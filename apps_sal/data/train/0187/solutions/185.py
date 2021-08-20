class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = 0
        max_profit = 0
        mark = 0
        waiting = 0
        n = len(customers)
        i = 0
        while i < n or waiting > 0:
            if i < n:
                waiting = waiting + customers[i]
            if waiting > 4:
                waiting = waiting - 4
                profit = profit + 4 * boardingCost
            else:
                profit = profit + waiting * boardingCost
                waiting = 0
            profit = profit - runningCost
            if profit > max_profit:
                max_profit = profit
                mark = i + 1
            i = i + 1
        return mark if max_profit > 0 else -1
