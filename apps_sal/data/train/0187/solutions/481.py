class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if (boardingCost * 4 <= runningCost):
            return -1

        posRotate = 0
        posProfit = 0

        rotate = 0
        profit = 0
        waiting = 0

        for item in customers:
            waiting += item
            if (waiting > 4):
                waiting -= 4
                profit += 4 * boardingCost - runningCost
            else:
                profit += waiting * boardingCost - runningCost
                waiting = 0
            rotate += 1

            if (profit > 0):
                posRotate = profit
                posRotate = rotate

        noRotate = waiting // 4
        remaining = waiting % 4

        rotate += noRotate
        profit += (4 * boardingCost * noRotate) - noRotate * runningCost

        if (profit > 0):
            posRotate = rotate
            posProfit = profit

        if (remaining * boardingCost > runningCost):
            posRotate += 1
            posProfit += remaining * boardingCost - runningCost

        if (posProfit <= 0):
            return -1
        return posRotate
