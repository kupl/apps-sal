class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        res = n + 1
        pre = {}
        pre[0] = -1
        dp = [float('inf')] * n
        p = 0
        for (i, a) in enumerate(arr):
            p += a
            dp[i] = dp[i - 1]
            if p - target in pre:
                cur = i - pre[p - target]
                if pre[p - target] >= 0 and dp[pre[p - target]] != float('inf'):
                    res = min(res, cur + dp[pre[p - target]])
                dp[i] = min(i - pre[p - target], dp[i - 1])
            pre[p] = i
        return -1 if res == n + 1 else res
