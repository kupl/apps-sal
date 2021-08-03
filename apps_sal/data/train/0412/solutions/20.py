class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        def solve(s, t):
            if s == 0:
                if t == 0:
                    return 1
                return 0
            if dp[s][t] != -1:
                return dp[s][t]
            ans = 0
            for i in range(1, f + 1):
                if t >= i:
                    ans += solve(s - 1, t - i)
            dp[s][t] = ans
            return dp[s][t]
        dp = [[-1] * (target + 1) for _ in range(d + 1)]
        return solve(d, target) % (10**9 + 7)
