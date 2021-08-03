class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0] * len(text2) for i in range(len(text1))]

        def helper(s1, s2, i1, i2):
            if not s1 or not s2:
                return 0
            if memo[i1][i2]:
                return memo[i1][i2]
            if s1[0] == s2[0]:
                memo[i1][i2] = 1 + helper(s1[1:], s2[1:], i1 + 1, i2 + 1)

            else:
                memo[i1][i2] = max(helper(s1[1:], s2, i1 + 1, i2), helper(s1, s2[1:], i1, i2 + 1))
            return memo[i1][i2]

        return helper(text1, text2, 0, 0)
