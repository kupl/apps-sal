class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit, max_t = 0, -1
        waiting, profit, t = 0, 0, 0
        while t < len(customers) or waiting > 0:
            if t < len(customers):
                waiting += customers[t]
            boarding = min(waiting, 4)
            waiting -= boarding
            profit += boardingCost * boarding - runningCost
            if profit > max_profit:
                max_profit, max_t = profit, t + 1
            t += 1
        return max_t

