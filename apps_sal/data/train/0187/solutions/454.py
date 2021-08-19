class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = 0
        customers_left = 0
        boarding_customers = 0
        i = 0
        max_round = 0
        while customers_left > 0 or i < len(customers):
            this_round = customers[i] if i < len(customers) else 0
            this_round += customers_left
            customers_left = 0
            if this_round > 4:
                customers_left = this_round - 4
                this_round = 4
            if (this_round + boarding_customers) * boardingCost - runningCost * (i + 1) > max_profit:
                max_profit = (this_round + boarding_customers) * boardingCost - runningCost * (i + 1)
                max_round = i + 1
            boarding_customers += this_round
            i += 1
        return max_round if max_profit > 0 else -1
