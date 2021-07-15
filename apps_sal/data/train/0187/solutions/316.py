class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        profits = []
        waitings = 0
        
        def boarding(waitings, profits):
            boardings = 0
            
            # out
            if waitings >= 4:
                boardings = 4
            else:
                boardings = waitings
            
            # calculate profit
            lastprofit = 0 if len(profits) == 0 else profits[len(profits) - 1]
            thisprofit = lastprofit + boardings * boardingCost - runningCost
            profits.append(thisprofit)
            
            return boardings
            
        def calculateBestTimes(profits):
            return profits.index(max(profits))
        
        for customer in customers:
            waitings += customer
            boardings = boarding(waitings, profits)
            waitings -= boardings
            
        while waitings > 0:
            boardings = boarding(waitings, profits)
            waitings -= boardings
            
        # print(profits)
        times = calculateBestTimes(profits)
        
        if profits[times] <= 0:
            times = -1
        else:
            times += 1
        
        return times
