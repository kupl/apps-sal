class Solution:

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        @lru_cache(None)
        def dfs(i: int, t: int, pc: int) -> int:
            if i == m:
                return math.inf if t != 0 else 0
            if houses[i] != 0:
                return dfs(i + 1, t - (pc != houses[i]), houses[i])
            else:
                return min((dfs(i + 1, t - (pc != c), c) + cost[i][c - 1] for c in range(1, n + 1)))
        ans = dfs(0, target, -1)
        return ans if ans != math.inf else -1
