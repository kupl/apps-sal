class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        for i in range(1, n + 1):
            for j in range(1, i):
                dp[i] = max(max(dp[j], j) * max(i - j, dp[i - j]), dp[i])
        return dp[-1]
