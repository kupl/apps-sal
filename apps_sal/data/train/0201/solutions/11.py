class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        dp = [1 for i in range(n + 1)]
        for i in range(2, n + 1):
            sums = 0
            for j in range(1, i + 1):
                sums += dp[j - 1] * dp[i - j]
            dp[i] = sums
        print(dp)
        return dp[-1]
