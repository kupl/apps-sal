class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        (i, queue) = (0, 0)
        (total_profit, max_profit) = (0, -1)
        result = -1
        while i < len(customers) or queue > 0:
            queue += 0 if i >= len(customers) else customers[i]
            board = min(queue, 4)
            total_profit += board * boardingCost - runningCost
            if max_profit < total_profit:
                max_profit = total_profit
                if max_profit > 0:
                    result = i
            queue -= board
            i += 1
        return result if result < 0 else result + 1
