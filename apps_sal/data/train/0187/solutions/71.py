class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = []
        profits = 0
        waiting = 0
        for i in range(len(customers)):
            waiting += customers[i]
            if waiting <= 4:
                profit.append(profits + waiting * boardingCost - runningCost)
                profits += waiting * boardingCost - runningCost
                waiting = 0
            else:
                profit.append(profits + 4 * boardingCost - runningCost)
                profits += 4 * boardingCost - runningCost
                waiting = waiting - 4
        while waiting > 4:
            profit.append(profits + 4 * boardingCost - runningCost)
            profits += 4 * boardingCost - runningCost
            waiting = waiting - 4
        profit.append(profits + waiting * boardingCost - runningCost)
        profits += waiting * boardingCost - runningCost
        x = max(profit)
        if x < 0:
            return -1
        else:
            return profit.index(x) + 1
