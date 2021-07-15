from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        n, m = len(text1), len(text2)
        
        @lru_cache(maxsize=10000)
        def lcs(i, j):
            if i > n-1 or j > m-1:
                return 0
            if text1[i] == text2[j]:
                return lcs(i+1, j+1) + 1
            return max(lcs(i+1, j), lcs(i, j+1))
            
        return lcs(0, 0)
                

