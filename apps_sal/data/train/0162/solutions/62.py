class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i < 0 or j < 0: return 0
            if text1[i] == text2[j]: return 1+dfs(i-1, j-1)
            return max(dfs(i, j-1), dfs(i-1, j))
        
        if not(text1 and text2): return 0
        n, m = len(text1), len(text2)
        return dfs(n-1, m-1)

