class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting, profit, maxProfit, res, start, total = 0, 0, 0, 0, 0, 0

        while start < len(customers) or waiting:
            waiting += customers[start] if start < len(customers) else 0
            onboard = min(4, waiting)
            waiting -= onboard
            total += onboard
            profit = boardingCost * total - (start + 1) * runningCost

            if maxProfit < profit:
                maxProfit = profit
                res = start + 1
            start += 1

        return res if maxProfit > 0 else -1
