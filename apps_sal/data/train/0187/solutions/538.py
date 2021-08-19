class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = 0
        max_step = -1
        profit = 0
        rest = 0
        for (i, c) in enumerate(customers):
            customer = c + rest
            (customer, rest) = (min(4, customer), max(0, customer - 4))
            profit += customer * boardingCost - runningCost
            if profit > max_profit:
                max_profit = profit
                max_step = i + 1
        (q, r) = divmod(rest, 4)
        if q > 0:
            profit += q * 4 * boardingCost - q * runningCost
            if profit > max_profit:
                max_profit = profit
                max_step = len(customers) + q
        if r > 0:
            profit += r * boardingCost - runningCost
            if profit > max_profit:
                max_step = len(customers) + q + 1
        return max_step
