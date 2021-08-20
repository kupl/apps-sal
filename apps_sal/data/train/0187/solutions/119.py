class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        cur_profit = 0
        max_profit = -1
        waiting_customers = 0
        ans = -1
        turn = 0
        for customer in customers:
            turn += 1
            waiting_customers += customer
            to_board = min(waiting_customers, 4)
            waiting_customers -= to_board
            cur_profit += -runningCost + to_board * boardingCost
            if cur_profit > max_profit:
                max_profit = cur_profit
                ans = turn
        while waiting_customers > 0:
            turn += 1
            to_board = min(waiting_customers, 4)
            waiting_customers -= to_board
            cur_profit += -runningCost + to_board * boardingCost
            if cur_profit > max_profit:
                max_profit = cur_profit
                ans = turn
        return ans if max_profit >= 0 else -1
