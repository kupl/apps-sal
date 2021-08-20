class Solution:

    def numTrees(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                print(j)
                print(i - j - 1)
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]
        '\n         :type n: int\n         :rtype: int\n         '
