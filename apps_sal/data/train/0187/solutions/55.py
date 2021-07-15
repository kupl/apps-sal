class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        maxCost = currCost= 0
        maxRound = -1
        currRound = 0
        waiting = 0
        boarded = 0
        for c in customers:
            waiting += c
            currRound += 1
            currBoard = (waiting if waiting < 4 else 4)
            boarded += currBoard
            currCost = (boarded*boardingCost) - (currRound*runningCost)
            waiting -= currBoard
            if currCost > maxCost:
                maxCost = currCost
                maxRound = currRound
        while waiting > 0:
            currRound += 1
            currBoard = (waiting if waiting < 4 else 4)
            boarded += currBoard
            currCost = (boarded*boardingCost) - (currRound*runningCost)
            waiting -= currBoard
            if currCost > maxCost:
                maxCost = currCost
                maxRound = currRound
        return maxRound

