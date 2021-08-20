class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        (m, n) = (len(A), len(B))
        if m == 0 or n == 0:
            return 0
        memo = dict()

        def dfs(i, j):
            if i == m or j == n:
                return 0
            if (i, j) in memo:
                return memo[i, j]
            res = max(dfs(i + 1, j), dfs(i, j + 1))
            if A[i] == B[j]:
                res = max(res, 1 + dfs(i + 1, j + 1))
            memo[i, j] = res
            return res
        return dfs(0, 0)
