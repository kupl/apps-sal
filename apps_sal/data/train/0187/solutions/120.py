class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        cur_profit = remainder_customers = steps = res = 0
        max_profit = -1
        for customer in customers:
            remainder_customers += customer
            getting_on = min(remainder_customers, 4)
            cur_profit += getting_on * boardingCost - runningCost
            remainder_customers -= getting_on
            steps += 1
            if cur_profit > max_profit:
                max_profit = cur_profit
                res = steps
        while remainder_customers > 0:
            getting_on = min(remainder_customers, 4)
            cur_profit += getting_on * boardingCost - runningCost
            remainder_customers -= getting_on
            steps += 1
            if cur_profit > max_profit:
                max_profit = cur_profit
                res = steps
        return -1 if max_profit < 0 else res
