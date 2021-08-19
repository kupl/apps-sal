class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}

        def dfs(n, t):
            if n == 0:
                return t == 0
            if (n, t) in memo:
                return memo[n, t]
            ret = 0
            for face in range(1, f + 1):
                ret += dfs(n - 1, t - face)
            memo[n, t] = ret % (10 ** 9 + 7)
            return memo[n, t]
        return dfs(d, target)
