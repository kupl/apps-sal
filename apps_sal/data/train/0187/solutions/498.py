class Solution:

    def minOperationsMaxProfit(self, customers, boardingCost: int, runningCost: int) -> int:
        count = 0
        (ans, profit) = (-1, 0)
        max_profit = 0
        i = 0
        while i < len(customers) or count > 0:
            if i < len(customers):
                count += customers[i]
            profit += boardingCost * min(count, 4) - runningCost
            count = max(0, count - 4)
            if profit > max_profit:
                ans = i + 1
                max_profit = profit
            i += 1
        return ans
