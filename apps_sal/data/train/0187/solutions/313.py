class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = []
        lastprofit = 0
        wait = customers[0]
        i = 0
        while i < len(customers) or wait > 0:
            if wait > 4:
                wait -= 4
                board = 4
            else:
                board = wait
                wait = 0
            profit.append(lastprofit + board * boardingCost - runningCost)
            lastprofit = profit[-1]
            i += 1
            if i < len(customers):
                wait += customers[i]
        ans = 0
        t = -1
        for (i, c) in enumerate(profit):
            if c > ans:
                ans = c
                t = i + 1
        return t
