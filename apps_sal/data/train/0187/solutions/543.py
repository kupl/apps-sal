class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        count = 0
        minCount = -1
        profit = 0
        maxProfit = None
        waiting = 0
        for (i, cnum) in enumerate(customers):
            waiting += cnum
            if waiting >= 4:
                rounds = waiting // 4
                count += rounds
                profit += (boardingCost * 4 - runningCost) * rounds
                waiting = waiting % 4
            elif count <= i:
                count += 1
                profit += boardingCost * waiting - runningCost
                waiting = 0
            if profit > 0 and (maxProfit is None or profit > maxProfit):
                maxProfit = profit
                minCount = count
        if waiting > 0:
            profit += boardingCost * waiting - runningCost
            count += 1
            if profit > 0 and (maxProfit is None or profit > maxProfit):
                maxProfit = profit
                minCount = count
        return minCount
