class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        def dfs(d, target):
            if (d, target) in cache:
                return cache[(d, target)]
            if target < 0 or d < 0:
                return 0
            if target == 0 and d == 0:
                return 1
            ways = 0
            for i in range(1, f + 1):
                ways += dfs(d - 1, target - i)
            cache[(d, target)] = ways
            return ways

        cache = {}
        mod = 10 ** 9 + 7
        return dfs(d, target) % mod
