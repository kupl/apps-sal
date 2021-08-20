class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boarding_cost: int, running_cost: int) -> int:
        customer = 0
        remained = 0
        max_profit = -1
        run = 0
        max_run = 0
        index = 0
        while remained or index < len(customers):
            run += 1
            remained += customers[index] if index < len(customers) else 0
            if remained < 4:
                customer += remained
                remained = 0
            else:
                customer += 4
                remained -= 4
            profit = customer * boarding_cost - run * running_cost
            if profit > max_profit:
                max_profit = profit
                max_run = run
            index += 1
        return -1 if max_profit < 0 else max_run
