class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        numCust = 0
        rotation = 0
        curWait = 0
        maxProfit = 0
        minRo = 0
        for i, customer in enumerate(customers):
            while rotation < i:
                rotation += 1
                curWait -= 4
                curWait = max(0, curWait)
                curProfit = (numCust - curWait) * boardingCost - rotation * runningCost
                if curProfit > maxProfit:
                    maxProfit = curProfit
                    minRo = rotation

            numCust += customer
            curWait += customer
            rots = curWait // 4
            rotation += rots
            curWait %= 4
            curProfit = (numCust - curWait) * boardingCost - rotation * runningCost
            if curProfit > maxProfit:
                maxProfit = curProfit
                minRo = rotation

        if curWait > 0:
            rotation += 1
            curProfit = numCust * boardingCost - rotation * runningCost
            if curProfit > maxProfit:
                maxProfit = curProfit
                minRo = rotation
        return minRo if maxProfit > 0 else -1
