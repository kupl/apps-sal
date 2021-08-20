class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        (curr, ans, waiting, profit) = (0, 0, 0, 0)
        for turn in range(len(customers)):
            waiting += customers[turn]
            boarding = 4 if 4 < waiting else waiting
            waiting -= boarding
            profit += boardingCost * boarding - runningCost
            if profit > curr:
                (curr, ans) = (profit, turn + 1)
        else:
            j = turn
            while waiting > 0:
                j += 1
                boarding = 4 if 4 < waiting else waiting
                waiting -= boarding
                profit += boardingCost * boarding - runningCost
                if profit > curr:
                    (curr, ans) = (profit, j + 1)
        return ans if profit > 0 else -1
