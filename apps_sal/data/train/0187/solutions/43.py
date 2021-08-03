class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if runningCost >= 4 * boardingCost or not customers:
            return -1
        tobeBoarded = 0
        minRound, maxProfit, profit = 0, 0, 0
        preRound = 0

        for i, x in enumerate(customers):
            tobeBoarded += x
            preRound = i + 1
            if tobeBoarded >= 4:
                tobeBoarded -= 4
                minRound = preRound
                maxProfit, profit = maxProfit + 4 * boardingCost - runningCost, profit + 4 * boardingCost - runningCost
            else:
                profit = tobeBoarded * boardingCost - runningCost
                tobeBoarded = 0
                if profit > maxProfit:
                    maxProfit = profit
                    minRound = preRound

        while tobeBoarded > 0:
            preRound += 1
            if tobeBoarded >= 4:
                tobeBoarded -= 4
                minRound = preRound
                maxProfit, profit = maxProfit + 4 * boardingCost - runningCost, profit + 4 * boardingCost - runningCost
            else:
                profit = profit + tobeBoarded * boardingCost - runningCost
                tobeBoarded = 0
                if profit > maxProfit:
                    maxProfit = profit
                    minRound = preRound
        return minRound
