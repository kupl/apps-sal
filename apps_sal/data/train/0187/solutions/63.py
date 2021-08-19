class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        res = -1
        n = len(customers)
        max_profit = 0
        current_customer = 0
        served_customer = 0
        current_profit = 0
        current_cost = 0
        for (i, v) in enumerate(customers):
            current_customer += v
            boarding_customer = 4 if current_customer >= 4 else current_customer
            served_customer += boarding_customer
            current_customer -= boarding_customer
            current_cost += runningCost
            current_profit = served_customer * boardingCost - current_cost
            if current_profit > max_profit:
                max_profit = current_profit
                res = i + 1
        i = n
        while current_customer > 0:
            i += 1
            boarding_customer = 4 if current_customer >= 4 else current_customer
            served_customer += boarding_customer
            current_customer -= boarding_customer
            current_cost += runningCost
            current_profit = served_customer * boardingCost - current_cost
            if current_profit > max_profit:
                max_profit = current_profit
                res = i
        return res
