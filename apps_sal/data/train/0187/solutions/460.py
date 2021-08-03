class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        wait = 0
        ans = -1
        max_profit = 0
        tb = 0
        total_rotate = max(len(customers), sum(customers) // 4 + 1)
        for i in range(total_rotate):
            if i < len(customers):
                total = wait + customers[i]
            else:
                total = wait
            board = min(4, total)
            tb += board
            wait = max(0, total - board)
            profit = tb * boardingCost - (i + 1) * runningCost
            if profit > max_profit:
                max_profit = profit
                ans = i + 1
        return ans
