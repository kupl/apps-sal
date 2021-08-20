class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        (n, m) = (len(text1), len(text2))
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for row in range(1, n + 1):
            for col in range(1, m + 1):
                if text1[row - 1] == text2[col - 1]:
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
        return dp[n][m]

    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:

        def helper(i1, i2):
            if (i1, i2) in self.memo:
                return self.memo[i1, i2]
            res = 0
            if i1 == len(text1) or i2 == len(text2):
                res = 0
            elif text1[i1] == text2[i2]:
                res = 1 + helper(i1 + 1, i2 + 1)
            else:
                res = max(helper(i1 + 1, i2), helper(i1, i2 + 1))
            self.memo[i1, i2] = res
            return self.memo[i1, i2]
        self.memo = {}
        return helper(0, 0)
