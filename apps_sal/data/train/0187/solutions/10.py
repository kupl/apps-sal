class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = []
        isFirst = True
        waiting = 0
        if runningCost > 4 * boardingCost:
            return -1
        for cust in customers:
            if isFirst:
                if cust + waiting >= 4:
                    waiting += cust - 4
                    profit.append(boardingCost * 4 - runningCost)
                else:
                    profit.append(boardingCost * (cust + waiting) - runningCost)
                    waiting = 0
                isFirst = False
            else:
                if cust + waiting >= 4:
                    waiting += cust - 4
                    profit.append(boardingCost * 4 - runningCost + profit[-1])
                else:
                    profit.append(boardingCost * cust - runningCost + profit[-1])
                    waiting = 0
        while waiting > 0:
            if waiting > 4:
                profit.append(boardingCost * 4 - runningCost + profit[-1])
                waiting -= 4
            else:
                profit.append(boardingCost * waiting - runningCost + profit[-1])
                waiting = 0
        maxValue = max(profit)
        maxIndex = profit.index(maxValue) + 1
        if maxValue > 0:
            return maxIndex
        else:
            return -1
