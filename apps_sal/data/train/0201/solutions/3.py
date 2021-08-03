class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            total = 0
            for j in range(i):
                total += (dp[j] * dp[i - j - 1])
            dp[i] = total

        return dp[n]
