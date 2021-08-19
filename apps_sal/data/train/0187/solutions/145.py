class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        (n, i, max_profit, waiting, profit, max_idx) = (len(customers), 0, 0, 0, 0, -1)
        while waiting > 0 or i < n:
            if i < n:
                waiting += customers[i]
            i += 1
            count = min(4, waiting)
            waiting -= count
            profit += count * boardingCost - runningCost
            if profit > max_profit:
                (max_profit, max_idx) = (profit, i)
        return max_idx
