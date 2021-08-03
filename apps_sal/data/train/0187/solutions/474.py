class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        rotations = 0
        profit = 0
        waiting = 0
        maxProfit = -1
        maxRotation = -1

        i = 0
        while i < len(customers) or waiting > 0:
            #print(i, waiting, profit, maxProfit, maxRotation)
            net = 0 - runningCost
            if i < len(customers):
                waiting += customers[i]
            if waiting > 0:
                boarding = min(4, waiting)
                waiting -= boarding
                net += (boardingCost * boarding)
            # print(net)
            profit += net
            if profit > maxProfit:
                maxProfit = profit
                maxRotation = i + 1
            i += 1

        return maxRotation
