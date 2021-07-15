from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        
        @lru_cache(None)
        def dp(s1, s2):
            if len(s1) == 0 or len(s2) == 0:
                return 0
            elif s1[0] == s2[0]:
                return 1 + dp(s1[1:], s2[1:])
            return max(dp(s1[1:], s2), dp(s1, s2[1:]))
        
        return dp(text1, text2)

