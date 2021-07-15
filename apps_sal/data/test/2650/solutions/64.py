from heapq import heappop, heappush
from typing import Optional


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
    def top(self) -> Optional[int]:
        """Return the minimum value if is_max_heap is False;
        otherwise, return the maximum value from the heap.
        If the heap is empty, None is returned.
        """
        while self._heap and self._heap[0] not in self._set:
            heappop(self._heap)
        if not self._heap:
            return None
        return self._heap[0] if not self.is_max_heap else -self._heap[0]

    def pop(self) -> Optional[int]:
        """Pop and return the minimum value if is_max_heap is False;
        otherwise, return the maximum value from the heap.
        If the heap is empty, None is returned.
        """
        while self._heap and self._heap[0] not in self._set:
            heappop(self._heap)
        if not self._heap:
            return None
        self.size -= 1
        res = heappop(self._heap)
        self._set.discard(res)
        return res if not self.is_max_heap else -res

    def push(self, value: int) -> None:
        """Push value into the heap."""
        if self.is_max_heap:
            value = -value
        if value in self._set:
            return
        self.size += 1
        heappush(self._heap, value)
        self._set.add(value)

    def delete(self, value: int) -> None:
        """Delete value from the heap."""
        if self.is_max_heap:
            value = -value
        if value not in self._set:
            return
        self.size -= 1
        self._set.discard(value)


def main():
    # https://atcoder.jp/contests/abc170/tasks/abc170_e
    N, _, *X = list(map(int, open(0).read().split()))
    AB, CD = X[: 2 * N], X[2 * N :]
    rate, belonging = [0] * (N + 1), [0] * (N + 1)
    kindy = [DeletableHeapq(is_max_heap=True) for _ in range(200_001)]

    for i, (a, b) in enumerate(zip(*[iter(AB)] * 2), 1):
        rate[i], belonging[i] = (a << 18) + i, b
        kindy[b].push(rate[i])

    smart_infants = DeletableHeapq(*(k.top for k in kindy if k.size))
    res = []
    for c, next_k in zip(*[iter(CD)] * 2):
        prev_k = belonging[c]
        belonging[c] = next_k

        for k in (prev_k, next_k):
            if kindy[k].size:
                smart_infants.delete(kindy[k].top)

        kindy[prev_k].delete(rate[c])
        kindy[next_k].push(rate[c])

        for k in (prev_k, next_k):
            if kindy[k].size:
                smart_infants.push(kindy[k].top)

        res.append(smart_infants.top >> 18)

    print(("\n".join(map(str, res))))


def __starting_point():
    main()

__starting_point()
