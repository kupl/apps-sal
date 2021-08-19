class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if 4 * boardingCost <= runningCost:
            return -1
        profit = 0
        pre_max = 0
        wait = 0
        ans = 0
        i = 0
        for c in customers:
            wait += c
            if wait > 0:
                profit += boardingCost * min(wait, 4) - runningCost
                if profit > pre_max:
                    ans = i + 1
                wait -= min(wait, 4)
            i += 1
            pre_max = max(pre_max, profit)
        while wait > 0:
            profit += boardingCost * min(wait, 4) - runningCost
            if profit > pre_max:
                ans = i + 1
            wait -= min(wait, 4)
            i += 1
            pre_max = max(pre_max, profit)
        if pre_max <= 0:
            return -1
        else:
            return ans
