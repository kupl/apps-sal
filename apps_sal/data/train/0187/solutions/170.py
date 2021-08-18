from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        cur = best = wheel_turns = 0
        best_idx = None
        waiting = 0
        capacity = 4

        while waiting or wheel_turns < len(customers):
            if wheel_turns < len(customers):
                waiting += customers[wheel_turns]

            wheel_turns += 1

            passengers = min(waiting, capacity)
            waiting -= passengers

            cur += (passengers * boardingCost) - runningCost

            if cur > best:
                best_idx = wheel_turns
                best = cur

        if best_idx is None:
            best_idx = -1

        return best_idx
