class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(arrLen, steps//2 + 1)
        dp = [0] * arrLen
        dp[0] = 1
        for i in range(steps):
            dp = [ (j - 1 >= 0 and dp[j-1] or 0) + dp[j] + (j + 1 < arrLen and dp[j+1] or 0) for j in range(arrLen)]
        return dp[0] % (10**9 + 7)

