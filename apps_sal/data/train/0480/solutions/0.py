# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/discuss/569521/7-python-approaches-with-Time-and-Space-analysis
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        r = min(arrLen, steps // 2 + 1)
        dp = [0, 1]
        for t in range(steps):
            dp[1:] = [sum(dp[i - 1:i + 2]) for i in range(1, min(r + 1, t + 3))]
        return dp[1] % (10**9 + 7)
