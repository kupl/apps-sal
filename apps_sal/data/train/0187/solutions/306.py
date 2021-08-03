import math


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        minRotation = 0
        MaxProfit = 0
        waiting = 0
        profit = 0
        for i in range(len(customers)):
            total = waiting + customers[i]
            if total >= 4:
                profit += 4 * boardingCost - runningCost
                if profit > MaxProfit:
                    MaxProfit = profit
                    minRotation = i + 1
                waiting = total - 4
            else:
                profit += total * boardingCost - runningCost
                if profit > MaxProfit:
                    MaxProfit = profit
                    minRotation = i + 1
                waiting = 0
        print(waiting)
        if waiting:
            temp = waiting
            print(((waiting // 4) * 4, int(waiting / 4)))
            profit += (waiting // 4) * 4 * boardingCost - runningCost * int(waiting / 4)
            if profit > MaxProfit:
                MaxProfit = profit
                minRotation = len(customers) + int(waiting / 4)
            waiting = waiting % 4
            profit += waiting * boardingCost - runningCost
            if profit > MaxProfit:
                return len(customers) + math.ceil(temp / 4)
        if minRotation > 0:
            return minRotation
        return -1
