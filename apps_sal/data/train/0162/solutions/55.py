class Solution:

    def longestCommonSubsequence(self, s1: str, s2: str) -> int:

        @lru_cache(None)
        def helper(s1, s2, i, j):
            if i == len(s1) or j == len(s2):
                return 0
            if s1[i] == s2[j]:
                return 1 + helper(s1, s2, i + 1, j + 1)
            else:
                return max(helper(s1, s2, i + 1, j), helper(s1, s2, i, j + 1))
        return helper(s1, s2, 0, 0)
