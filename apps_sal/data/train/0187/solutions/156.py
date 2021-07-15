from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        def boarders():
            waiters = 0
            for c in customers:
                waiters += c
                cur = min(4, waiters)
                waiters -= cur
                yield cur
            while waiters > 0:
                cur = min(4, waiters)
                waiters -= cur
                yield cur

        max = 0
        max_idx = -1
        cur = 0
        for i, b in enumerate(boarders()):
            cur += (b * boardingCost) - runningCost
            if cur > max:
                max = cur
                max_idx = i + 1

        return max_idx

