class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        totalCust = 0
        n = len(customers)
        ct = 0
        curr = 0
        profit = 0
        res = 0
        maxx = -999999
        pt = 0
        while True:
            ct += 1
            if pt < n:
                totalCust += customers[pt]
                pt += 1
            if totalCust < 4:
                curr += totalCust
                totalCust = 0
                profit = curr * boardingCost - ct * runningCost
                if maxx < profit:
                    maxx = profit
                    res = ct
                if pt == n:
                    break
            else:
                totalCust -= 4
                curr += 4
                profit = curr * boardingCost - ct * runningCost
                if maxx < profit:
                    maxx = profit
                    res = ct
        if profit > 0:

            return res
        else:
            return -1
