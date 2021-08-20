class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}
        MOD = pow(10, 9) + 7

        def dfs(d_left=d, target_left=target):
            if (d_left, target_left) in memo:
                return memo[d_left, target_left]
            if not d_left:
                return 1 if not target_left else 0
            else:
                memo[d_left, target_left] = 0
                for face in range(1, min(f + 1, target_left + 1)):
                    memo[d_left, target_left] += dfs(d_left - 1, target_left - face)
                return memo[d_left, target_left]
        return dfs() % MOD
