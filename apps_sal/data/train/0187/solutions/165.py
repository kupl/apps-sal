class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        curr_waiting = 0
        (curr_profit, max_profit, curr_op, max_profit_ops) = (0, 0, 0, 0)
        for c in customers:
            curr_op += 1
            curr_waiting += c
            num_boarded = min(4, curr_waiting)
            curr_waiting -= num_boarded
            curr_profit += boardingCost * num_boarded - runningCost
            if curr_profit > max_profit:
                max_profit = curr_profit
                max_profit_ops = curr_op
        while curr_waiting:
            curr_op += 1
            num_boarded = min(4, curr_waiting)
            curr_waiting -= num_boarded
            curr_profit += boardingCost * num_boarded - runningCost
            if curr_profit > max_profit:
                max_profit = curr_profit
                max_profit_ops = curr_op
        return max_profit_ops if max_profit > 0 else -1
