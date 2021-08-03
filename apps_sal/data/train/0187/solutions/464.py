class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        onboard = rotates = 0
        waiting = 0
        profit = 0
        rotates = 0
        while rotates < len(customers) or waiting > 0:
            if rotates < len(customers):
                waiting += customers[rotates]
            if waiting > 0:
                onboard += min(4, waiting)
                waiting -= min(4, waiting)
            rotates += 1
            p = onboard * boardingCost - runningCost * rotates
            if p > profit:
                profit = p
                ans = rotates

        return ans if profit > 0 else -1
