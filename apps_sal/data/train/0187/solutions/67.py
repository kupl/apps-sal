class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        q = 0
        r = 0
        profit = 0
        cnt = 0
        max_profit = -float('inf')
        while q > 0 or r < len(customers):
            if profit > max_profit:
                cnt = r
                max_profit = profit
            if r < len(customers):
                q += customers[r]
            if q >= 4:
                profit += boardingCost * 4 - runningCost
                q -= 4
            else:
                profit += boardingCost * q - runningCost
                q = 0
            r += 1
        if profit > max_profit:
            cnt = r
        return cnt if max_profit > 0 else -1
