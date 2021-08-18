from heapq import *
from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        counter = Counter(arr)
        size = len(arr)

        if len(counter) == size:
            return (size - 1) // 2 + 1

        max_heap = [(-freq, value) for value, freq in list(counter.items())]
        heapify(max_heap)

        removed = 0
        removed_size = 0

        while removed < size // 2:
            count, value = heappop(max_heap)
            count = -count
            removed += count
            removed_size += 1

        return removed_size
