class Solution:

    def minOperationsMaxProfit(self, C: List[int], B: int, R: int) -> int:
        res = i = cur = wait = 0
        idx = -1
        while i < len(C) or wait:
            if i < len(C):
                wait += C[i]
            i += 1
            cur += B * min(4, wait) - R
            wait -= min(4, wait)
            if cur > res:
                res = cur
                idx = i
        return idx if idx > 0 else -1
