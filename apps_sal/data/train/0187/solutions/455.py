class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = []
        wheel = [0, 0, 0, 0]
        wait = customers[0]
        t = 0
        maxt = len(customers)
        curProfit = 0
        while wait + sum(wheel) or t < maxt:
            if wait >= 4:
                wheel = [3, 3, 3, 3]
                wait -= 4
                curProfit += 4 * boardingCost
            elif wait == 3:
                wheel = [3, 3, 3, max(0, wheel[3] - 1)]
                wait = 0
                curProfit += 3 * boardingCost
            elif wait == 2:
                wheel = [3, 3, max(0, wheel[2] - 1), max(0, wheel[3] - 1)]
                wait = 0
                curProfit += 2 * boardingCost
            elif wait == 1:
                wheel = [3, max(0, wheel[1] - 1), max(0, wheel[2] - 1), max(0, wheel[3] - 1)]
                wait = 0
                curProfit += 1 * boardingCost
            elif wait == 0:
                wheel = [max(0, wheel[0] - 1), max(0, wheel[1] - 1), max(0, wheel[2] - 1), max(0, wheel[3] - 1)]
                wait = 0
            curProfit -= runningCost
            t += 1
            if t < maxt:
                wait += customers[t]
            profit.append(curProfit)
        res = -1
        maxprofit = 0
        for i in range(len(profit)):
            if profit[i] > maxprofit:
                res = i + 1
                maxprofit = profit[i]
        return res
