class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        (i, waiting) = (0, 0)
        (total_profit, max_profit) = (0, 0)
        result = -1
        while i < len(customers) or waiting > 0:
            waiting += 0 if i >= len(customers) else customers[i]
            board = min(waiting, 4)
            total_profit += board * boardingCost - runningCost
            if max_profit < total_profit:
                max_profit = total_profit
                result = i
            waiting -= board
            i += 1
        return result if result < 0 else result + 1
