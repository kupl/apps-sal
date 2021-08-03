class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        res = -1
        profit = 0
        maxProfit = 0
        custs = 0
        i = 0
        while i < len(customers) or custs != 0:
            if i < len(customers):
                custs += customers[i]
            profit += min(custs, 4) * boardingCost - runningCost
            custs -= min(custs, 4)
            if profit > maxProfit:
                maxProfit = profit
                res = i + 1
            i += 1
        return res
