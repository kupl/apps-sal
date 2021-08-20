class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def LCS(t1, t2):
            if len(t1) == 0 or len(t2) == 0:
                return 0
            elif t1[-1] == t2[-1]:
                return LCS(t1[0:-1], t2[0:-1]) + 1
            else:
                return max(LCS(t1[0:-1], t2), LCS(t1, t2[0:-1]))
        return LCS(text1, text2)
