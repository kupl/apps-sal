class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        best_r = -2
        best_p = 0
        profit = 0

        i, waiting = 0, 0
        while i < len(customers) or waiting > 0:
            if i < len(customers):
                waiting += customers[i]
            take = min(4, waiting)
            waiting -= take
            profit += take * boardingCost - runningCost
            if profit > best_p:
                best_p = profit
                best_r = i
            i += 1

        return best_r + 1
