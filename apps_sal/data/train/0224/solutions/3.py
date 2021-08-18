class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        row = len(s) + 1
        col = len(t) + 1
        dp = [0] * col
        dp[0] = 1
        for i in range(1, row):
            pre = dp[:]
            for j in range(1, col):
                if s[i - 1] == t[j - 1]:
                    dp[j] += pre[j - 1]
        return dp[-1]
