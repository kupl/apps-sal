class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_board = 0
        waiting = 0
        profit = 0
        i = 1
        maxv = float('-inf')
        res = None
        c_i = 0
        while c_i < len(customers) or waiting > 0:
            if c_i < len(customers):
                waiting += customers[c_i]
            tmp = min(waiting, 4)
            max_board += tmp
            waiting -= tmp
            profit = max_board * boardingCost - runningCost * i
            if profit > maxv:
                maxv = profit
                res = i
            i += 1
            c_i += 1
        return -1 if maxv < 0 else res
