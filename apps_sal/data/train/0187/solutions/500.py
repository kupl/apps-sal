class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = 0
        max_profit = float('-inf')
        n = len(customers)
        waiting = 0
        rotations = 0
        for i in range(n):
            cust = waiting + customers[i]
            profit += min(cust, 4) * boardingCost - runningCost
            if profit > max_profit:
                max_profit = profit
                rotations = i
            cust -= min(cust, 4)
            waiting = cust

        if waiting > 0:
            profit += (waiting // 4) * (4 * boardingCost - runningCost)
            if profit > max_profit:
                max_profit = profit
                rotations += waiting // 4
            waiting %= 4
            profit += waiting * boardingCost - runningCost
            if profit > max_profit:
                max_profit = profit
                rotations += 1

        return rotations + 1 if max_profit >= 0 else -1
