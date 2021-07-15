class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if runningCost>4*boardingCost:
            return -1
        maxp = -1
        maxd = 0
        day = 0
        profit=0
        remaining = 0
        for c in customers:
            to_board = min(4,c+remaining)
            remaining = max(remaining-to_board+c,0)
            day+=1
            profit = profit+ to_board*boardingCost-runningCost
            if profit>=maxp:
                maxd = day
                maxp = profit
        while to_board:
            to_board = min(4,remaining)
            remaining = max(remaining-to_board,0)
            day+=1
            profit = profit+ to_board*boardingCost-runningCost
            if profit>maxp:
                maxd = day
                maxp = profit
        return maxd
