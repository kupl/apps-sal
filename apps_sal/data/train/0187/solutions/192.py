class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 4 < runningCost:
            return -1
        if boardingCost * 4 == runningCost:
            return 0
        i = 0
        res = 0
        curM = 0
        cur = 0
        remind = 0
        served = 0
        for i in range(len(customers)):
            remind += customers[i]
            served += min(remind, 4)
            remind = max(0, remind - 4)
            cur = served * boardingCost - (i + 1) * runningCost
            if cur > curM:
                curM = cur
                res = i + 1

        if remind * boardingCost - runningCost <= 0:
            return res
        res = len(customers)
        while min(4, remind) * boardingCost - runningCost > 0:
            remind -= min(4, remind)
            res += 1
        return res

        total = sum(customers)
        if (total % 4) * boardingCost <= runningCost:
            return total // 4
        return total // 4 + 1
