from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0
        
        t1_idx = len(text1) - 1
        t2_idx = len(text2) - 1
        
        @lru_cache(maxsize=2147483647)
        def lcs(t1_idx, t2_idx):
            if t1_idx == -1 or t2_idx == -1:
                return 0
            if text1[t1_idx] == text2[t2_idx]:
                return 1 + lcs(t1_idx - 1, t2_idx - 1)
            else:
                return max(lcs(t1_idx, t2_idx - 1), lcs(t1_idx - 1, t2_idx))
        
        return lcs(t1_idx, t2_idx)
