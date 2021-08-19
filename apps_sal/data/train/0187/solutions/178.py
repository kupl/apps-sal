class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        remain = 0
        profit = 0
        maxProfit = -float('inf')
        maxId = -1
        for (i, val) in enumerate(customers):
            total = remain + val
            if total > 4:
                profit += 4 * boardingCost
                remain = total - 4
            else:
                profit += total * boardingCost
                remain = 0
            profit -= runningCost
            if profit > maxProfit:
                maxId = i
                maxProfit = profit
        j = maxId + 1
        while remain > 0:
            profit += min(remain, 4) * boardingCost - runningCost
            if profit > maxProfit:
                maxId = j
                maxProfit = profit
            remain = max(remain - 4, 0)
            j = j + 1
        if maxProfit <= 0:
            return -1
        else:
            return maxId + 1
