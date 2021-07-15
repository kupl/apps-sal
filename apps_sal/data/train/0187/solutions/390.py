class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_i, max_profit = -1, 0
        remain, board = 0, 0     
        i = 0
        while i < len(customers) or remain > 0:
            if i < len(customers):
                remain += customers[i]
            i += 1
            board += min(remain, 4)
            profit = board*boardingCost - i*runningCost
            if profit > max_profit:
                max_i = i
                max_profit = profit
            remain = max(0, remain-4)

        return max_i

