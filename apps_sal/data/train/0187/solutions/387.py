class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        runningProfit = []
        waiting = 0
        for arriving in customers:
            waiting += arriving
            boarding = min(4, waiting)
            waiting -= boarding
            currentProfit = boarding * boardingCost - runningCost
            if runningProfit:
                runningProfit.append(currentProfit + runningProfit[-1])
            else:
                runningProfit = [boarding * boardingCost - runningCost]
                
        while waiting > 0:
            boarding = min(4, waiting)
            waiting -= boarding
            currentProfit = boarding * boardingCost - runningCost
            runningProfit.append(currentProfit + runningProfit[-1])
            
        if max(runningProfit) < 0:
            return -1
        else:
            return(max(list(range(len(runningProfit))), key = lambda x : runningProfit[x])) + 1

