class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def LCS(s1, s2, i1, i2):
            if i1 > len(s1) - 1 or i2 > len(s2) - 1:
                return 0
            if (i1, i2) in memo:
                return memo[i1, i2]
            if s1[i1] == s2[i2]:
                memo[i1, i2] = 1 + LCS(s1, s2, i1 + 1, i2 + 1)
                return memo[i1, i2]
            s1_next = LCS(s1, s2, i1 + 1, i2)
            s2_next = LCS(s1, s2, i1, i2 + 1)
            memo[i1, i2] = max(s1_next, s2_next)
            return memo[i1, i2]
        return LCS(text1, text2, 0, 0)
