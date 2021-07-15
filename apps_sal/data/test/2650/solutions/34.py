from heapq import heappop, heappush
from typing import Optional


class DeletableHeapq:
    """Deletable Heapq: a heapq that supports lazy deletion of values."""

    __slots__ = ["_is_max_heap", "_set", "_heap"]

    def __init__(self, *initial_values: int, is_max_heap: bool = False) -> None:
        self._is_max_heap = is_max_heap
        self._set = set()
        self._heap = []

        if initial_values:
            for v in initial_values:
                self.push(v)

    def __len__(self) -> int:
        return len(self._set)

    @property
    def is_empty(self) -> bool:
        """Return whether the heap has no values or not."""
        return len(self) == 0

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
        return self._heap[0] if not self._is_max_heap else -self._heap[0]

    def push(self, value: int) -> None:
        """Push value into the heap."""
        if self._is_max_heap:
            value = -value
        if value in self._set:
            return
        heappush(self._heap, value)
        self._set.add(value)

    def delete(self, value: int) -> None:
        """Delete value from the heap."""
        if self._is_max_heap:
            value = -value
        if value not in self._set:
            return
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

    smarts = DeletableHeapq(*(k.top for k in kindy if not k.is_empty))
    res = []
    for c, d in zip(*[iter(CD)] * 2):
        prev_k, next_k = kindy[belonging[c]], kindy[d]
        belonging[c] = d

        for k in (prev_k, next_k):
            if not k.is_empty:
                smarts.delete(k.top)

        prev_k.delete(rate[c])
        next_k.push(rate[c])

        for k in (prev_k, next_k):
            if not k.is_empty:
                smarts.push(k.top)

        res.append(smarts.top >> 18)

    print(("\n".join(map(str, res))))


def __starting_point():
    main()

__starting_point()
