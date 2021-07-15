class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        def dfs(i, j, memo):
            if (i, j) not in memo:
                if j-i <= 1: return 0
                memo[(i, j)] = float('inf')
                for c in cuts:
                    if c > i and c < j:
                        memo[(i, j)] = min(memo[(i, j)], j-i+dfs(i, c, memo)+dfs(c, j, memo))
            return memo[(i, j)] if memo[(i, j)] != float('inf') else 0
        return dfs(0, n, dict())
