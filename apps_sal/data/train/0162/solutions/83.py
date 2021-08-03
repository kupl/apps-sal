class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #         dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]

        #         # logic: if same, add 1, else max(try each without first)
        #         # if row,col V == same, == prev diag + 1
        #         # else: = max(row-1,col, row,col-1)

        #         for row in range(1, len(text2) + 1):
        #             for col in range(1, len(text1) + 1):
        #                 if text2[row - 1] == text1[col - 1]:
        #                     dp[row][col] = dp[row-1][col-1] + 1
        #                 else:
        #                     dp[row][col] = max(dp[row-1][col], dp[row][col-1])

        #         return dp[-1][-1]
        from functools import lru_cache

        memo = {}

        def lcs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(text1) or j == len(text2):
                r = 0
            elif text1[i] == text2[j]:
                r = 1 + lcs(i + 1, j + 1)
            else:
                r = max(lcs(i + 1, j), lcs(i, j + 1))

            memo[(i, j)] = r
            return r

        return lcs(0, 0)
