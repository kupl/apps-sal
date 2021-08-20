import math


class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        maxx = 0
        ans = -1
        profit = 0
        waiting = 0
        i = 0
        while i < len(customers) or waiting > 0:
            if i < len(customers):
                waiting += customers[i]
            profit -= runningCost
            if waiting > 4:
                profit += 4 * boardingCost
                waiting -= 4
            else:
                profit += waiting * boardingCost
                waiting = 0
            if profit > maxx:
                ans = i
                maxx = profit
            i += 1
        return ans + 1 if ans > -1 else -1
