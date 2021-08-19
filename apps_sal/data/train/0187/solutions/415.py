class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        customers_line = 0
        current_customers = 0
        max_profit = -1
        number_rot = -1
        for (idx, customer) in enumerate(customers):
            customers_line += customer
            current_customers += min(4, customers_line)
            customers_line -= min(4, customers_line)
            if max_profit < boardingCost * current_customers - runningCost * (idx + 1):
                max_profit = boardingCost * current_customers - runningCost * (idx + 1)
                number_rot = idx + 1
        while customers_line > 0:
            idx += 1
            current_customers += min(4, customers_line)
            customers_line -= min(4, customers_line)
            if max_profit < boardingCost * current_customers - runningCost * (idx + 1):
                max_profit = boardingCost * current_customers - runningCost * (idx + 1)
                number_rot = idx + 1
        return number_rot
