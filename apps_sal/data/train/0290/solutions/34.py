class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        @lru_cache(None)
        def dfs(i, j):
            if i == j:
                return 0
            tot = float('inf')
            for k in range(len(cuts)):
                if i < cuts[k] < j:
                    tot = min(tot, dfs(i, cuts[k]) + dfs(cuts[k], j) + j - i)
            if tot == float('inf'):
                return 0
            return tot
        return dfs(0, n)
