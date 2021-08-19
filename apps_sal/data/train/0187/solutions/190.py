class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = served = onboard = max_round = max_profit = 0
        cur_round = 1
        while cur_round <= len(customers) or waiting > 0:
            if cur_round <= len(customers):
                waiting += customers[cur_round - 1]
            if waiting > 4:
                onboard = 4
                waiting -= onboard
            else:
                onboard = waiting
                waiting = 0
            served += onboard
            cur_profit = served * boardingCost - cur_round * runningCost
            if cur_profit > max_profit:
                max_profit = cur_profit
                max_round = cur_round
            cur_round += 1
        return max_round if max_profit > 0 else -1
