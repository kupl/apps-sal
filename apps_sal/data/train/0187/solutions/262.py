class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if 4 * boardingCost - runningCost <= 0:
            return -1
        max_profit = 0
        max_rotation = 0
        cum_profit = 0
        wait = 0
        for (i, c) in enumerate(customers):
            total = c + wait
            if total <= 4:
                board = total
            else:
                board = 4
            wait = total - board
            profit = board * boardingCost - runningCost
            cum_profit += profit
            if cum_profit > max_profit:
                max_profit = cum_profit
                max_rotation = i + 1
        if wait > 0:
            (div, mod) = divmod(wait, 4)
            cum_profit += div * (4 * boardingCost - runningCost)
            if cum_profit > max_profit:
                max_profit = cum_profit
                max_rotation += div
            re = mod * boardingCost - runningCost
            if re > 0:
                cum_profit += re
                if cum_profit > max_profit:
                    max_profit = cum_profit
                    max_rotation += 1
        if max_rotation == 0:
            return -1
        else:
            return max_rotation
