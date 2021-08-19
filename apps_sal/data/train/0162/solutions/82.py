"""
     text2 a c e
         0 1 2 3
text1 0  0 0 0 0
    a 1  0 1 1 1
    b 2  0 1 1 1
    c 3  0 1 2 2
    d 4  0 1 2 2
    e 5  0 1 2 3
"""


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        (m, n) = (len(text1) + 1, len(text2) + 1)
        dp = [[0] * n for _ in range(m)]
        res = 0
        for i in range(1, m):
            for j in range(1, n):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                res = max(res, dp[i][j])
        return res
