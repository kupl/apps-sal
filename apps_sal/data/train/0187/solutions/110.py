from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        cur = best = 0
        best_idx = None
        waiting = 0
        capacity = 4

        for idx, nxt in enumerate(customers):
            waiting += nxt
            passengers = min(waiting, capacity)
            waiting -= passengers

            cur += (passengers * boardingCost) - runningCost

            if cur > best:
                best_idx = idx + 1
                best = cur

        while waiting:
            idx += 1
            passengers = min(waiting, capacity)
            waiting -= passengers

            cur += (passengers * boardingCost) - runningCost

            if cur > best:
                best_idx = idx + 1
                best = cur

        if best_idx is None:
            best_idx = -1

        return best_idx
