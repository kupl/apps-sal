class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        wating = 0
        profit = 0
        idx = -1
        t_r = 0
        max_profit = 0
        for customer in customers:
            wating += customer
            if wating <= 4:
                profit += wating * boardingCost - runningCost
                wating = 0
            else:
                profit += 4 * boardingCost - runningCost
                wating -= 4
            t_r += 1
            if profit > max_profit:
                idx = t_r
                max_profit = profit
        if wating > 0:
            if 4 * boardingCost > runningCost:
                idx += wating // 4
        wating = wating % 4
        if wating * boardingCost > runningCost:
            idx += 1
        return idx
