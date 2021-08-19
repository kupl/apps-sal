class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        (curr, ans, waiting, profit) = (0, 0, 0, 0)
        for (turn, customers) in enumerate(customers):
            waiting += customers
            boarding = min(4, waiting)
            waiting -= boarding
            profit += boardingCost * boarding - runningCost
            if profit > curr:
                (curr, ans) = (profit, turn + 1)
        else:
            j = turn
            while waiting > 0:
                j += 1
                boarding = min(4, waiting)
                waiting -= boarding
                profit += boardingCost * boarding - runningCost
                if profit > curr:
                    (curr, ans) = (profit, j + 1)
        return ans if profit > 0 else -1
