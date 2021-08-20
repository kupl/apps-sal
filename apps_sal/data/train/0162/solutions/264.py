class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]
        to_return = 0
        for i in range(len(text2)):
            for j in range(len(text1)):
                (r, c) = (i + 1, j + 1)
                if text1[j] == text2[i]:
                    dp[r][c] = 1 + dp[r - 1][c - 1]
                else:
                    dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])
                to_return = max(to_return, dp[r][c])
        return to_return
