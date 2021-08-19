class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def recurse(i1, i2):
            if i1 >= len(text1) or i2 >= len(text2):
                return 0
            if (i1, i2) in memo:
                return memo[i1, i2]
            if text1[i1] == text2[i2]:
                memo[i1, i2] = 1 + recurse(i1 + 1, i2 + 1)
            else:
                memo[i1, i2] = max(recurse(i1 + 1, i2), recurse(i1, i2 + 1))
            return memo[i1, i2]
        return recurse(0, 0)
