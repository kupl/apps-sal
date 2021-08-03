class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0 for _ in range(m)] for _ in range(n)]

        # i -> text2
        # j -> text1
        for i in range(n):
            for j in range(m):
                # Need to do j-1, i-1, otherwise we would start from 1
                # on both strings
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + (0 if i - 1 < 0 or j - 1 < 0 else dp[i - 1][j - 1])
                else:
                    if i - 1 > -1:
                        dp[i][j] = dp[i - 1][j]
                    if j - 1 > -1:
                        dp[i][j] = max(dp[i][j], dp[i][j - 1])

        return dp[-1][-1]
