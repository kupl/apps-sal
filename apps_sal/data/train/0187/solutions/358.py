class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        maxi = 0
        maxRotate = -1
        profit = 0
        onBoarded = 0
        inQueue = 0
        rotates = 0
        for c in customers:
            rotates += 1
            onBoarded = max(0, onBoarded - 1)
            inQueue += c
            board = min(4, inQueue)
            inQueue -= board
            profit += board * boardingCost - runningCost
            if profit > maxi:
                maxi = profit
                maxRotate = rotates

        while inQueue > 0:
            rotates += 1
            onBoarded = max(0, onBoarded - 1)
            board = min(4, inQueue)
            inQueue -= board
            profit += board * boardingCost - runningCost
            if profit > maxi:
                maxi = profit
                maxRotate = rotates

        return maxRotate
