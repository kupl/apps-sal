class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[0] = 1

        for x in range(2, n + 1):
            for y in range(1, x + 1):
                dp[x] += (dp[y - 1] * dp[x - y])

        return dp[-1]
