from heapq import heappop, heappush

encode_kindy = lambda x, y: -((x << 18) + y)
decode_kindy = lambda x: (-x >> 18, -x & ((1 << 18) - 1))
encode_smarts = lambda x, y, z: ((x << 36) + (y << 18) + z)
decode_smarts_rate = lambda x: x >> 36


class DeletableHeapq:
    def __init__(self, *initial_values):
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
        return self._heap[0]

    def pop(self):
        while self._heap and self._heap[0] not in self._set:
            heappop(self._heap)
        if not self._heap:
            return None
        res = heappop(self._heap)
        self._set.discard(res)
        self.size -= 1
        return res

    def push(self, x):
        self.size += 1
        heappush(self._heap, x)
        self._set.add(x)

    def delete(self, x):
        self.size -= 1
        self._set.discard(x)


def main():
    N, _, *X = list(map(int, open(0).read().split()))
    AB, CD = X[: 2 * N], X[2 * N:]
    rate, belonging = [0] * (N + 1), [0] * (N + 1)
    kindy = [DeletableHeapq() for _ in range(200_001)]

    for i, (a, b) in enumerate(zip(*[iter(AB)] * 2), 1):
        rate[i], belonging[i] = a, b
        kindy[b].push(encode_kindy(a, i))

    smart_infants = DeletableHeapq(
        *(encode_smarts(*decode_kindy(k.top), i) for i, k in enumerate(kindy) if k.size)
    )

    res = []
    for c, next_k in zip(*[iter(CD)] * 2):
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

    print(("\n".join(map(str, res))))


def __starting_point():
    main()


__starting_point()
