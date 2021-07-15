class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        run = 0
        maxRun = 0
        profit = 0
        maxProfit = 0
        total = 0
        i = 0
        n = len(customers)
        while total > 0 or i < n:
            if i < n:
                total += customers[i]
                i += 1
            group = min(4, total)
            total -= group
            profit = profit + group*boardingCost - runningCost
            run += 1
            if profit > maxProfit:
                maxProfit = profit
                maxRun = run
                
        return maxRun if maxProfit > 0 else -1

