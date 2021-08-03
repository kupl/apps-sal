class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        cur_profit = remainder_customers = steps = res = 0
        max_profit = -1
        for customer in customers:
            remainder_customers += customer
            gettting_on = min(remainder_customers, 4)
            cur_profit += gettting_on * boardingCost - runningCost
            remainder_customers -= gettting_on
            steps += 1

            if cur_profit > max_profit:
                max_profit = cur_profit
                res = steps

        while remainder_customers > 0:
            gettting_on = min(remainder_customers, 4)
            cur_profit += gettting_on * boardingCost - runningCost
            remainder_customers -= gettting_on
            steps += 1

            if cur_profit > max_profit:
                max_profit = cur_profit
                res = steps

        return -1 if max_profit < 0 else res
