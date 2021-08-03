class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1, 2]
        if n < 3:
            return dp[n]
        for i in range(3, n + 1):

            dp.append(sum(dp[j - 1] * dp[i - j] for j in range(1, i + 1)))
        return dp[n]
