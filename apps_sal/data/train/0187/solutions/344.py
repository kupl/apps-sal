class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        iteration = 0
        max_profit = 0
        profit = 0
        wait = 0
        for i, c in enumerate(customers):
            wait += c
            board = min(4, wait)
            wait -= board
            if i == len(customers) - 1 and wait > 0:
                customers += [wait]
                wait = 0
            profit += boardingCost * board - runningCost
            if profit > max_profit:
                max_profit = profit
                iteration = i

        return iteration + 1 if max_profit > 0 else -1
