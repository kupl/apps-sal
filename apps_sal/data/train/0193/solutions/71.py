from collections import *


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = Counter()
        for num in arr:
            d[num] += 1

        counts = list(d.values())

        counts.sort(reverse=True)

        total = 0
        for (i, count) in enumerate(counts):
            total += count
            if total >= len(arr) // 2:
                return i + 1

        return None  # should never reach here
