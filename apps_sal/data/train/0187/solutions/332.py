class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = []
        total_customer = 0
        cur_profit = 0
        for (i, n) in enumerate(customers):
            total_customer += n
            cur_profit += min(total_customer, 4) * boardingCost - runningCost
            total_customer -= min(total_customer, 4)
            profit.append(cur_profit)
        import numpy as np
        while total_customer > 0:
            cur_profit += min(total_customer, 4) * boardingCost - runningCost
            total_customer -= min(total_customer, 4)
            profit.append(cur_profit)
        return np.argmax(profit) + 1 if max(profit) > 0 else -1
