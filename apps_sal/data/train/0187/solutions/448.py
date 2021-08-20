class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        (profit, waiting) = (0, 0)
        (max_profit, max_profit_rotations) = (0, 0)
        for (i, ppl) in enumerate(customers):
            waiting += ppl
            if waiting > 0:
                entry = min(4, waiting)
                profit += boardingCost * entry - runningCost
                waiting -= entry
                if profit > max_profit:
                    max_profit = profit
                    max_profit_rotations = i + 1
        while waiting > 0:
            i += 1
            entry = min(4, waiting)
            profit += boardingCost * entry - runningCost
            waiting -= entry
            if profit > max_profit:
                max_profit = profit
                max_profit_rotations = i + 1
        return max_profit_rotations if max_profit_rotations > 0 else -1
