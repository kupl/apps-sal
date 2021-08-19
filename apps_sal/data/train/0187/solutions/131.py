class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profits = []
        curr_profit = 0
        ppl_waiting = 0
        for (i, ppl) in enumerate(customers):
            ppl_waiting += ppl
            num_board = min(4, ppl_waiting)
            curr_profit += num_board * boardingCost - runningCost
            profits.append(curr_profit)
            ppl_waiting -= num_board
        while ppl_waiting:
            num_board = min(4, ppl_waiting)
            curr_profit += num_board * boardingCost - runningCost
            profits.append(curr_profit)
            ppl_waiting -= num_board
        max_prof = max(profits)
        if max_prof <= 0:
            return -1
        return profits.index(max_prof) + 1
