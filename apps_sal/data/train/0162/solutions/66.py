class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        n1 = len(text1)
        n2 = len(text2)
        dp = [[0 for _ in range(n2 + 1)] for _ in range(2)]

        for i in range(n1 + 1):
            for j in range(n2 + 1):
                if i == 0 or j == 0:
                    dp[i % 2][j] = 0
                else:
                    if text1[i - 1] == text2[j - 1]:
                        dp[i % 2][j] = dp[1 - i % 2][j - 1] + 1
                    else:
                        dp[i % 2][j] = max(dp[1 - i % 2][j], dp[i % 2][j - 1])
        return dp[n1 % 2][n2]
