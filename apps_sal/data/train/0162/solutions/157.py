class Solution:

    def longestCommonSubsequence(self, s1: str, s2: str) -> int:

        @lru_cache(maxsize=10 ** 18)
        def LCS(s1, s2, n1, n2):
            if n1 == 0 or n2 == 0:
                return 0
            if s1[n1 - 1] == s2[n2 - 1]:
                return 1 + LCS(s1, s2, n1 - 1, n2 - 1)
            else:
                return max(LCS(s1, s2, n1 - 1, n2), LCS(s1, s2, n1, n2 - 1))
        return LCS(s1, s2, len(s1), len(s2))
