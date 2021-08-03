class Solution:
    def soupServings(self, N: int) -> float:
        if N > 4800:
            return 1

        @lru_cache(None)
        def dfs(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            return (dfs(a - 100, b) + dfs(a - 75, b - 25) + dfs(a - 50, b - 50) + dfs(a - 25, b - 75)) / 4
        return dfs(N, N)
