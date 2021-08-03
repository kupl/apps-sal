class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        inLine = 0
        profit = 0
        maxProf = -1
        maxRoll = -1
        rolls = 0
        for i in customers:
            inLine += i
            if inLine >= 4:
                profit += 4 * boardingCost - runningCost
                inLine -= 4
            else:
                profit += inLine * boardingCost - runningCost
                inLine = 0
            rolls += 1

            if profit > maxProf:
                maxProf = profit
                maxRoll = rolls

        while inLine:
            if inLine >= 4:
                profit += 4 * boardingCost - runningCost
                inLine -= 4
            else:
                profit += inLine * boardingCost - runningCost
                inLine = 0
            rolls += 1
            # maxProf = max(maxProf, profit)
            if profit > maxProf:
                maxProf = profit
                maxRoll = rolls

        return maxRoll
