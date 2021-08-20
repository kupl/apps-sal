class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        board = 0
        wait = 0
        rotation = 0
        maxProfit = 0
        maxRotation = -1
        for n in customers:
            wait += n
            if wait > 4:
                board += 4
                wait -= 4
            else:
                board += wait
                wait = 0
            rotation += 1
            profit = board * boardingCost - rotation * runningCost
            if profit > maxProfit:
                maxProfit = profit
                maxRotation = rotation
        while wait > 0:
            if wait > 4:
                board += 4
                wait -= 4
            else:
                board += wait
                wait = 0
            rotation += 1
            profit = board * boardingCost - rotation * runningCost
            if profit > maxProfit:
                maxProfit = profit
                maxRotation = rotation
        return maxRotation
