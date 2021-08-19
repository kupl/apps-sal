class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if runningCost >= boardingCost * 4:
            return -1
        result = -1
        maxProfit = 0
        waiting = 0
        current = 0
        for (i, customerCount) in enumerate(customers):
            waiting += customerCount
            boarding = min(waiting, 4)
            waiting -= boarding
            current += boarding * boardingCost - runningCost
            if current > maxProfit:
                maxProfit = current
                result = i + 1
        if waiting > 0:
            fullRoundsLeft = waiting // 4
            lastRoundQuantity = waiting % 4
            current += fullRoundsLeft * (4 * boardingCost - runningCost)
            turns = len(customers) + fullRoundsLeft
            if current > maxProfit:
                maxProfit = current
                result = turns
            current += lastRoundQuantity * boardingCost - runningCost
            turns += 1
            if current > maxProfit:
                maxProfit = current
                result = turns
        return result if result >= 0 else -1
