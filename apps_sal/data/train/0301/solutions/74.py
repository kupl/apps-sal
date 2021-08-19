class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        (M, N) = (len(A), len(B))

        @lru_cache(None)
        def dfs(i, j):
            if i == M or j == N:
                return 0
            if A[i] == B[j]:
                return 1 + dfs(i + 1, j + 1)
            else:
                return max(dfs(i + 1, j), dfs(i, j + 1))
        return dfs(0, 0)
