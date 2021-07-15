class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        res = round = profit = max_profit = remain = i = 0
        while remain or i < len(customers):
            if i < len(customers):
                remain += customers[i]
                i += 1
            on_board = min(4, remain)
            remain -= on_board
            profit += boardingCost * on_board - runningCost
            round += 1
            if profit > max_profit:
                max_profit = profit
                res = round
        return res if max_profit > 0 else -1
