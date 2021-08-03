class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        rotations, profit = 0, 0
        ret, max_profit = 0, 0
        waiting = 0

        for c in customers:
            waiting += c
            profit += min(4, waiting) * boardingCost - runningCost
            waiting -= min(4, waiting)
            rotations += 1
            if profit > max_profit:
                max_profit = profit
                ret = rotations
        if waiting:
            profit += waiting // 4 * (4 * boardingCost - runningCost)
            rotations += waiting // 4
            if profit > max_profit:
                max_profit = profit
                ret = rotations
            waiting %= 4

        if waiting:
            profit += waiting * boardingCost - runningCost
            rotations += 1
            if profit > max_profit:
                max_profit = profit
                ret = rotations

        return ret if max_profit > 0 else -1
