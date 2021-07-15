class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        '''
        Two-row DP solution. dp[i][j] = # of ways to get to position j in i steps.
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1] (need to take care of boundary conditions on first/last)
        This is guarantee to be unique # of ways because we just look at what's the last step taken (stay, left, or right).
        The final answer is dp[steps][0]
        '''
        arrLen = min(steps // 2 + 1, arrLen)
        dp = [0] * arrLen
        dp[0], dp[1] = 1, 1
        for i in range(2, steps):
            dp_new = [0] * arrLen
            for j in range(min(i + 1,arrLen)):
                dp_new[j] = (dp[j - 1] if (j - 1) >= 0 else 0) + dp[j] + (dp[j + 1] if (j + 1) < arrLen else 0)
            dp = dp_new
        return (dp[0] + dp[1]) % (10**9 + 7)

