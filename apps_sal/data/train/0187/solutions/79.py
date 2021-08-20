from typing import List


class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if runningCost >= boardingCost * 4:
            return -1
        max_profit = 0
        num_rotations = 0
        curr_profit = 0
        curr_rotations = 0
        curr_waiting = 0
        for num_customers in customers:
            curr_waiting += num_customers
            taking = min(curr_waiting, 4)
            curr_profit += taking * boardingCost - runningCost
            curr_rotations += 1
            curr_waiting -= taking
            if curr_profit > max_profit:
                max_profit = curr_profit
                num_rotations = curr_rotations
        while curr_waiting:
            taking = min(curr_waiting, 4)
            curr_profit += taking * boardingCost - runningCost
            curr_rotations += 1
            curr_waiting -= taking
            if curr_profit > max_profit:
                max_profit = curr_profit
                num_rotations = curr_rotations
        return num_rotations if max_profit > 0 else -1
