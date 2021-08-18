class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        currentProfit = 0
        highestProfitSoFar = 0
        maxProfit = 0
        stoppedForMaxProft = 0
        timesStopped = 1
        currentWaiting = 0
        totalBoarded = 0
        i = 0
        while i < len(customers) or currentWaiting > 0:
            if i < len(customers):
                currentWaiting += customers[i]
            totalBoarded += min(4, currentWaiting)
            currentProfit = totalBoarded * boardingCost - timesStopped * runningCost
            currentWaiting -= min(4, currentWaiting)
            if currentProfit > highestProfitSoFar:
                highestProfitSoFar = currentProfit
                stoppedForMaxProft = timesStopped
            timesStopped += 1
            i += 1
        if stoppedForMaxProft == 0:
            return -1
        return stoppedForMaxProft
