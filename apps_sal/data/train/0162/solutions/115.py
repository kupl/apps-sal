class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def helper(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i, j) in memo:
                return memo[i, j]
            if text1[i] == text2[j]:
                memo[i, j] = 1 + helper(i + 1, j + 1)
                return memo[i, j]
            else:
                memo[i, j] = max(helper(i, j + 1), helper(i + 1, j))
                return memo[i, j]
        return helper(0, 0)
