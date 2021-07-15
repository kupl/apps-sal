class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        q = 0
        profit = 0
        best_profit = 0
        rotation = 0
        customers_served = 0
        min_rotation = -1
        i = 0
        while q or i < len(customers):
            rotation += 1
            if i < len(customers):
                q += customers[i]
                i += 1
            if q > 0:
                customers_served += min(q, 4)
                profit =  customers_served * boardingCost - rotation * runningCost
                q = max(0, q - 4)
                if profit > best_profit:
                    min_rotation = rotation
                    best_profit = profit
        return min_rotation
