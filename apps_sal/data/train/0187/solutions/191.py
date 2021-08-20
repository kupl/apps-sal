class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        board = customers[0]
        profit = 0
        prevprofit = 0
        best = -1
        i = 1
        k = 0
        while board > 0 or i != len(customers):
            k += 1
            sub = min(board, 4)
            profit += sub * boardingCost - runningCost
            board -= sub
            if profit > prevprofit and profit > 0:
                best = k
            if i < len(customers):
                board += customers[i]
                i += 1
            prevprofit = profit
        return best
