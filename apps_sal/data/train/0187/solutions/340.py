class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        (max_profit, min_rotations) = (0, -1)
        curr_profit = 0
        (waiting, rotations) = (0, 0)
        customers.reverse()
        while curr_profit >= 0:
            if customers:
                waiting += customers.pop()
            if waiting == 0:
                if not customers:
                    break
            else:
                curr_profit += min(4, waiting) * boardingCost - runningCost
                waiting -= min(4, waiting)
            rotations += 1
            if curr_profit > max_profit:
                (max_profit, min_rotations) = (curr_profit, rotations)
        return min_rotations
