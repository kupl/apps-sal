class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        cur = 0
        p = 0
        ans = float('-inf')
        t = 0
        ff = 0
        for c in customers:
            cur += c
            cnt = min(cur, 4)
            cur -= cnt
            p += cnt * boardingCost
            p -= runningCost
            t += 1
            if p > ans:
                ans = p
                ff = t

        while cur > 0:
            cnt = min(cur, 4)
            cur -= cnt
            p += cnt * boardingCost
            p -= runningCost
            t += 1
            if p > ans:
                ans = p
                ff = t

        return -1 if ans <= 0 else ff
