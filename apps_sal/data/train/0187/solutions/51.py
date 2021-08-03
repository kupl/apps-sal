class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waitingNum = 0
        highest = 0
        res = 0
        # print(profit)
        index = 0
        for i in customers:
            waitingNum += i

            if waitingNum >= 4:
                profit = 4 * boardingCost - runningCost
                waitingNum -= 4
            else:
                profit = waitingNum * boardingCost - runningCost
                waitingNum = 0
            if highest + profit > highest:
                res = index + 1
                highest = highest + i

            index += 1
        while waitingNum != 0:
            if waitingNum >= 4:
                profit = 4 * boardingCost - runningCost
                waitingNum -= 4
            else:
                profit = waitingNum * boardingCost - runningCost
                waitingNum = 0
            if highest + profit > highest:
                res = index + 1
                highest = highest + i

            index += 1
        if res == 0:
            return -1
        return res
