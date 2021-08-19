class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        (n_board, n_wait) = (0, 0)
        (cur_profit, max_profit, max_idx) = (0, -float('inf'), -1)
        for (i, people) in enumerate(customers):
            n_wait += people
            n_board += min(4, n_wait)
            n_wait -= min(4, n_wait)
            cur_profit = boardingCost * n_board - (i + 1) * runningCost
            if cur_profit > max_profit:
                max_profit = cur_profit
                max_idx = i + 1
        while n_wait:
            i += 1
            n_board += min(n_wait, 4)
            n_wait -= min(n_wait, 4)
            cur_profit = boardingCost * n_board - (i + 1) * runningCost
            if cur_profit > max_profit:
                max_profit = cur_profit
                max_idx = i + 1
        return max_idx if max_profit > 0 else -1
