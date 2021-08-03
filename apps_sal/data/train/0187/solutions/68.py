class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = 0
        answ = -1
        waiting = 0
        profit = 0
        i = 0
        n = len(customers)

        while i < n or waiting > 0:
            if i < n:
                waiting += customers[i]
            if waiting >= 4:
                profit += 4 * boardingCost - runningCost
                waiting -= 4
            elif waiting > 0:
                profit += waiting * boardingCost - runningCost
                waiting = 0
            else:
                profit -= runningCost

            if max_profit < profit:
                max_profit = profit
                answ = i + 1

            i += 1

        return answ
