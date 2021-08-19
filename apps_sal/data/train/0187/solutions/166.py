from collections import deque


class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        customers = deque(customers)
        in_line = profit = rot = best_rot = 0
        max_profit = -1
        while customers or in_line:
            c = customers.popleft() if customers else 0
            in_line += c
            board = min(in_line, 4)
            in_line -= board
            profit += board * boardingCost
            rot += 1
            profit -= runningCost
            if profit > max_profit:
                max_profit = profit
                best_rot = rot
        return best_rot if max_profit > 0 else -1
