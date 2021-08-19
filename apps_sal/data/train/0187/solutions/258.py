class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = wait = 0
        i = 0
        r = m = -1
        while i < len(customers) or wait:
            if i < len(customers):
                wait += customers[i]
            board = min(4, wait)
            profit += board * boardingCost - runningCost
            wait -= board
            i += 1
            if profit > m:
                r = i
                m = profit
        return r
