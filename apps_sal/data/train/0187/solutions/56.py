class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = 0
        num_rotations = 0
        min_rotations = 0
        curr_profit = 0
        max_profit = 0
        for customer in customers:
            waiting += customer
            if waiting >= 4:
                can_board = 4
                waiting -= 4
            else:
                can_board = waiting
                waiting = 0
            num_rotations += 1
            curr_profit += can_board * boardingCost - runningCost
            if curr_profit > max_profit:
                max_profit = curr_profit
                min_rotations = num_rotations
        while waiting:
            if waiting >= 4:
                can_board = 4
                waiting -= 4
            else:
                can_board = waiting
                waiting = 0
            num_rotations += 1
            curr_profit += can_board * boardingCost - runningCost
            if curr_profit > max_profit:
                max_profit = curr_profit
                min_rotations = num_rotations
        if min_rotations == 0:
            return -1
        return min_rotations
