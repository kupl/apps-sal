class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        boarded = 0
        waiting = 0
        mpy = -1
        rotations = -1
        for i in range(len(customers)):
            waiting += customers[i]
            if waiting >= 4:
                boarded += 4
                waiting -= 4
            else:
                waiting = 0
                boarded += waiting
            bP = boarded * boardingCost
            rC = (i + 1) * runningCost
            profit = bP - rC
            if profit > mpy:
                rotations = i + 1
                mpy = profit

        r = i + 1
        while waiting > 0:
            if waiting >= 4:
                waiting -= 4
                boarded += 4
            else:
                boarded += waiting
                waiting = 0

            r += 1
            bP = boarded * boardingCost
            rC = r * runningCost
            profit = bP - rC
            if profit > mpy:
                rotations = r
                mpy = profit
        if mpy > 0:
            return rotations
        else:
            return -1
