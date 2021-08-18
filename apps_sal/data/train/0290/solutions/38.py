class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        return self.dfs(cuts, 0, n, dict())

    def dfs(self, cuts, i, j, memo):
        if j - i <= 1:
            return 0
        if (i, j) not in memo:
            memo[(i, j)] = float('inf')
            for c in cuts:
                if c > i and c < j:
                    memo[(i, j)] = min(memo[(i, j)], j - i + self.dfs(cuts, i, c, memo) + self.dfs(cuts, c, j, memo))
            if memo[(i, j)] == float('inf'):
                memo[(i, j)] = 0
        return memo[(i, j)]
