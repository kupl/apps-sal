class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profits = []
        boarded = 0
        waiting = 0
        i = 0
        while waiting != 0 or i < len(customers):
            if i < len(customers):
                waiting = waiting + customers[i]
            boarded = boarded + min(4, waiting)
            waiting = waiting - min(4, waiting)
            profit = boardingCost * boarded - (i + 1) * runningCost
            profits.append(profit)
            i = i + 1

        if max(profits) > 0:

            return profits.index(max(profits)) + 1
        else:
            return -1
