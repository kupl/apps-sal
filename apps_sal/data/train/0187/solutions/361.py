class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = 0
        best_rots = -1
        rots = 0
        waiting = 0
        boarded = 0
        c = 0
        while waiting > 0 or c<len(customers):
            if c<len(customers):
                waiting += customers[c]
            if waiting > 4:
                boarded += 4
                waiting -= 4
            else:
                boarded += waiting
                waiting = 0
            rots += 1
            profit = boarded*boardingCost - rots*runningCost
            if profit > max_profit:
                max_profit = profit
                best_rots = rots
            c += 1
        return best_rots
