class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        total_customers = 0
        max_profit = 0
        no_rotation = 0
        pending = 0
        i = 0
        while i < len(customers) or pending > 0:
            if i < len(customers):
                pending += customers[i]
            if pending >= 4:
                pending -= 4
                total_customers += 4
            else:
                total_customers += pending
                pending = 0
            profit = total_customers * boardingCost - (i + 1) * runningCost
            if profit > max_profit:
                max_profit = profit
                no_rotation = (i + 1)
            i += 1
        if no_rotation == 0:
            return -1
        return no_rotation
