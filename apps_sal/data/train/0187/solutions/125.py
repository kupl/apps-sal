class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        curr_profit, curr_rotate = 0, 0
        best_profit, best_rotate = -1, 0
        queue_count = 0
        for customer in customers:
            queue_count += customer
            board_count = min(queue_count, 4)
            curr_profit += board_count * boardingCost - runningCost
            curr_rotate += 1
            queue_count -= board_count
            if curr_profit > best_profit:
                best_profit, best_rotate = curr_profit, curr_rotate
        while queue_count > 0:
            board_count = min(queue_count, 4)
            curr_profit += board_count * boardingCost - runningCost
            curr_rotate += 1
            queue_count -= board_count
            if curr_profit > best_profit:
                best_profit, best_rotate = curr_profit, curr_rotate
        return best_rotate if best_profit > 0 else -1
