class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        @lru_cache(None)
        def dfs(i, j):
            if i == -1 or j == -1:
                return 0
            if A[i] == B[j]:
                return dfs(i - 1, j - 1) + 1
            
            return max(dfs(i - 1, j), dfs(i, j - 1))
        
        return dfs(m - 1, n - 1)
