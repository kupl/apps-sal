class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        @lru_cache(None)
        def find(i, j):
            if i >= m or j >= n:
                return 0
            if text1[i] == text2[j]:
                return 1+find(i+1, j+1)
            else:
                return max(find(i+1, j), find(i, j+1))
        
        return find(0, 0)
            

