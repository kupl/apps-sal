class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        left = 0
        profit = 0
        max_profit = 0
        max_ret = -1
        ret = 0
        for x in customers:
            left += x
            if left >= 4:
                profit += (4 * boardingCost - runningCost)
                left -= 4
            else:
                profit += (left * boardingCost - runningCost)
                left = 0
            ret += 1
            if profit > max_profit:
                max_ret = ret
                max_profit = profit
        while left > 0:
            if left >= 4:
                profit += (4 * boardingCost - runningCost)
                left -= 4
            else:
                profit += (left * boardingCost - runningCost)
                left = 0
            ret += 1
            if profit > max_profit:
                max_ret = ret
                max_profit = profit
        return max_ret
