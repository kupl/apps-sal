class Solution:
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        if 4 * boardingCost - runningCost <= 0:
            return -1

        n = len(customers)
        wait = 0
        now_profit = 0
        max_profit = 0
        res = -1
        for i in range(n):
            wait += customers[i]
            now_profit += boardingCost * min(wait, 4) - runningCost
            wait -= min(wait, 4)
            if now_profit > max_profit:
                max_profit = now_profit
                res = i + 1
        res += (wait // 4)
        if boardingCost * (wait % 4) - runningCost > 0:
            res += 1
        return res
