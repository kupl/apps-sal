from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        
        @lru_cache(None)
        def lcs(idxA, idxB):
            if idxA < 0 or idxB < 0:
                return 0

            if text1[idxA] == text2[idxB]:
                return 1 + lcs(idxA - 1, idxB - 1)

            return max(lcs(idxA - 1, idxB), lcs(idxA, idxB - 1))

        return lcs(len(text1) - 1, len(text2) - 1)
            
            

