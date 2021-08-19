class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boarding_cost: int, running_cost: int) -> int:
        if len(customers) == 0:
            return 0
        if boarding_cost * 4 <= running_cost:
            return -1
        available_customer_count = 0
        customers_per_rotation = []
        for i in range(len(customers)):
            available_customer_count += customers[i]
            customers_per_rotation.append(min(available_customer_count, 4))
            available_customer_count -= customers_per_rotation[-1]
        while available_customer_count > 0:
            customers_per_rotation.append(min(available_customer_count, 4))
            available_customer_count -= customers_per_rotation[-1]
        max_profit = 0
        max_turn = -1
        previous_profit = 0
        current_customer_count = 0
        for (i, customer_count) in enumerate(customers_per_rotation):
            current_customer_count += customer_count
            profit = current_customer_count * boarding_cost - running_cost * (i + 1)
            if profit > max_profit:
                max_profit = profit
                max_turn = i + 1
        return max_turn
