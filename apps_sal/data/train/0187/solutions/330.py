class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        earn = 0
        max_earn = 0
        men = 0
        cnt = 0
        res = -1
        for c in customers:
            cnt += 1
            men += c
            earn += min(men, 4) * boardingCost
            earn -= runningCost
            if earn > max_earn:
                max_earn = earn
                res = cnt
            men -= min(men, 4)
        while men > 0:
            cnt += 1
            earn += min(men, 4) * boardingCost
            earn -= runningCost
            if earn > max_earn:
                max_earn = earn
                res = cnt
            men -= min(men, 4)
        return res
