class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        (ans, max_profit) = (-1, 0)
        waiting = 0
        profit = 0
        i = 0
        while waiting > 0 or i < len(customers):
            if i < len(customers):
                waiting += customers[i]
            if waiting >= 4:
                waiting -= 4
                boarded = 4
            else:
                boarded = waiting
                waiting = 0
            max_profit += boardingCost * boarded - runningCost
            if max_profit > 0 and max_profit > profit:
                ans = i + 1
                profit = max_profit
            i += 1
        return ans
