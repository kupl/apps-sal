class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if not customers:
            return 0
        waiting = 0
        op = 0
        maxProfit = -1
        index = 0
        total_boarding = 0
        for (i, people) in enumerate(customers):
            op += 1
            waiting += people
            boarding = min(4, waiting)
            total_boarding += boarding
            currProfit = total_boarding * boardingCost - op * runningCost
            waiting -= boarding
            if currProfit > maxProfit:
                maxProfit = currProfit
                index = op
        while waiting > 0:
            op += 1
            boarding = min(waiting, 4)
            total_boarding += boarding
            currProfit = total_boarding * boardingCost - op * runningCost
            waiting -= boarding
            if currProfit > maxProfit:
                maxProfit = currProfit
                index = op
        if maxProfit == -1:
            return -1
        else:
            return index
