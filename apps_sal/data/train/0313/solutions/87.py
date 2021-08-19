from typing import List


class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def condition(numDays: int) -> bool:
            (flowers, bouquets) = (0, 0)
            for bloom in bloomDay:
                if numDays < bloom:
                    flowers = 0
                else:
                    bouquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            return bouquets >= m
        if len(bloomDay) < m * k:
            return -1
        (low, high) = (min(bloomDay), max(bloomDay))
        while low < high:
            mid = low + (high - low) // 2
            if condition(mid):
                high = mid
            else:
                low = mid + 1
        return low
