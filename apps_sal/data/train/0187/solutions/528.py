class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profits = [0] * (13 * len(customers))
        p_cursor = 0
        waiting = 0
        for c in customers:
            waiting += c
            riding = min(waiting, 4)
            profits[p_cursor] += boardingCost * riding
            profits[p_cursor] -= runningCost
            if p_cursor > 0:
                profits[p_cursor] += profits[p_cursor - 1]
            p_cursor += 1
            waiting -= riding

        while waiting > 0:
            riding = min(waiting, 4)
            profits[p_cursor] += boardingCost * riding
            profits[p_cursor] -= runningCost
            if p_cursor > 0:
                profits[p_cursor] += profits[p_cursor - 1]
            p_cursor += 1
            waiting -= riding

        max_profit = max(profits)
        if max_profit <= 0:
            return -1

        for i, p in enumerate(profits):
            if p == max_profit:
                return i + 1

        return -1
