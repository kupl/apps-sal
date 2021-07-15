class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting_customers = cur_profit = max_profit = rounds = 0
        max_profit_round = -1
        customers.reverse()
        while waiting_customers > 0 or customers:
            if customers:
                waiting_customers += customers.pop()
            cur_profit += min(waiting_customers, 4) * boardingCost - runningCost
            waiting_customers -= min(waiting_customers, 4)
            rounds += 1
            if max_profit < cur_profit:
                max_profit = cur_profit
                max_profit_round = rounds
        return max_profit_round
