class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = customers[0]
        idx = 1
        current_profit = 0
        max_profit = -1
        rotated = 0
        max_rotated = -1
        while waiting > 0 or idx < len(customers):
            rotated += 1
            can_board = min(4, waiting)
            current_profit += can_board * boardingCost - runningCost
            if current_profit > max_profit:
                max_profit = max(current_profit, max_profit)
                max_rotated = rotated
            waiting -= can_board
            if idx < len(customers):
                waiting += customers[idx]
                idx += 1
            # print(current_profit, max_profit, rotated, max_rotated)

        return max_rotated
