class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = 0
        maxprofit = 0
        maxi = -1
        wait = 0
        i = 0
        for customer in customers:
            i += 1
            wait += customer
            on = min(wait, 4)
            wait -= on
            profit += on * boardingCost - runningCost
            if profit > maxprofit:
                maxprofit = profit
                maxi = i
        while wait:
            i += 1
            on = min(wait, 4)
            wait -= on
            profit += on * boardingCost - runningCost
            if profit > maxprofit:
                maxprofit = profit
                maxi = i
        return maxi
