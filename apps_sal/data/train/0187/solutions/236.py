class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        cust = waiting = rot = i = 0
        max_profit = profit_at = 0
        while waiting or i < len(customers):
            if i < len(customers):
                waiting += customers[i]
            i += 1

            reduce = min(4, waiting)
            cust += reduce
            waiting -= reduce
            rot += 1
            profit = cust * boardingCost - (rot) * runningCost
            if profit > max_profit:
                max_profit = profit
                profit_at = rot
        return profit_at if profit_at > 0 else -1
