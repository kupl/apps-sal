class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        su = ans = ans_ind = p = ind = 0
        for a in customers:
            ind += 1
            su += a
            m = min(4, su)
            p += m * boardingCost - runningCost
            su -= m
            if p > ans:
                ans = p
                ans_ind = ind
        while su:
            ind += 1
            m = min(4, su)
            p += m * boardingCost - runningCost
            su -= m
            if p > ans:
                ans = p
                ans_ind = ind
        return ans_ind if ans > 0 else -1
