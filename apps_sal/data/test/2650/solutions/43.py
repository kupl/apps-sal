from heapq import heappop, heappush


class DeletableHeapq:
    """Deletable Heapq: A heapq supporting lazy deletion of values."""

    def __init__(self, *initial_values: int, is_max_heap: bool = False) -> None:
        self.is_max_heap = is_max_heap
        self.size = 0
        self._set = set()
        self._heap = []
        if initial_values:
            for v in initial_values:
                self.push(v)

    @property
    def top(self):
        while self._heap and self._heap[0] not in self._set:
            heappop(self._heap)
        if not self._heap:
            return None
        return self._heap[0] if not self.is_max_heap else -self._heap[0]

    def pop(self):
        while self._heap and self._heap[0] not in self._set:
            heappop(self._heap)
        if not self._heap:
            return None
        self.size -= 1
        res = heappop(self._heap)
        self._set.discard(res)
        return res if not self.is_max_heap else -res

    def push(self, value):
        if value is None:
            return
        if self.is_max_heap:
            value = -value
        if value in self._set:
            return
        self.size += 1
        heappush(self._heap, value)
        self._set.add(value)

    def delete(self, value):
        if value is None:
            return
        if self.is_max_heap:
            value = -value
        if value not in self._set:
            return
        self.size -= 1
        self._set.discard(value)


def main():

    def encode_kindy(x, y):
        return (x << 18) + y

    def decode_kindy(x):
        return (x >> 18, x & (1 << 18) - 1)

    def encode_smarts(x, y, z):
        return (x << 36) + (y << 18) + z

    def decode_smarts_rate(x):
        return x >> 36
    (N, _, *X) = list(map(int, open(0).read().split()))
    (AB, CD) = (X[:2 * N], X[2 * N:])
    (rate, belonging) = ([0] * (N + 1), [0] * (N + 1))
    kindy = [DeletableHeapq(is_max_heap=True) for _ in range(200001)]
    for (i, (a, b)) in enumerate(zip(*[iter(AB)] * 2), 1):
        (rate[i], belonging[i]) = (a, b)
        kindy[b].push(encode_kindy(a, i))
    smart_infants = DeletableHeapq(*(encode_smarts(*decode_kindy(k.top), i) for (i, k) in enumerate(kindy) if k.size))
    res = []
    for (c, next_k) in zip(*[iter(CD)] * 2):
        prev_k = belonging[c]
        belonging[c] = next_k
        for k in (prev_k, next_k):
            if kindy[k].size:
                smart_infants.delete(encode_smarts(*decode_kindy(kindy[k].top), k))
        kindy[prev_k].delete(encode_kindy(rate[c], c))
        kindy[next_k].push(encode_kindy(rate[c], c))
        for k in (prev_k, next_k):
            if kindy[k].size:
                smart_infants.push(encode_smarts(*decode_kindy(kindy[k].top), k))
        res.append(decode_smarts_rate(smart_infants.top))
    print('\n'.join(map(str, res)))


def __starting_point():
    main()


__starting_point()
