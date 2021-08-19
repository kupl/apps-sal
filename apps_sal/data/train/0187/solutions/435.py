class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        rotate = 0
        ans = -1
        maxProfit = 0
        profit = 0
        remaining = 0
        i = 0
        while i < len(customers) or remaining:
            if i < len(customers):
                remaining += customers[i]
                i += 1
            boarding = min(remaining, 4)
            remaining -= boarding
            rotate += 1
            profit += boarding * boardingCost - runningCost
            if profit > maxProfit:
                maxProfit = profit
                ans = rotate
        return ans
