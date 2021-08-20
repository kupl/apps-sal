class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost << 2 <= runningCost:
            return -1
        waitingCustomers = 0
        curProfit = 0
        maxProfit = 0
        maxProfitTurns = 0
        curTurn = 0
        for nCust in customers:
            curTurn += 1
            waitingCustomers += nCust
            if waitingCustomers > 0:
                boardedCustomers = min(4, waitingCustomers)
                waitingCustomers -= boardedCustomers
                curProfit += boardedCustomers * boardingCost
            curProfit -= runningCost
            if curProfit > maxProfit:
                maxProfit = curProfit
                maxProfitTurns = curTurn
        fullLoads = waitingCustomers >> 2
        remLoad = waitingCustomers & 3
        curProfit += (fullLoads * boardingCost << 2) - runningCost * fullLoads
        curTurn += fullLoads
        if curProfit > maxProfit:
            maxProfit = curProfit
            maxProfitTurns = curTurn
        if remLoad > 0:
            curProfit += remLoad * boardingCost - runningCost
            curTurn += 1
            if curProfit > maxProfit:
                maxProfit = curProfit
                maxProfitTurns = curTurn
        if curProfit > maxProfit:
            return curTurn
        if maxProfit == 0:
            return -1
        else:
            return maxProfitTurns
