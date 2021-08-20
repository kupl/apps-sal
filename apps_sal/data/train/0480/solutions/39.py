class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7

        def dp(x, s, memo):
            if s == 0:
                if x == 0:
                    return 1
                else:
                    return 0
            if (x, s) not in memo:
                if x == 0:
                    memo[x, s] = (dp(x + 1, s - 1, memo) + dp(x, s - 1, memo)) % MOD
                elif x == arrLen - 1:
                    memo[x, s] = (dp(x - 1, s - 1, memo) + dp(x, s - 1, memo)) % MOD
                else:
                    memo[x, s] = (dp(x + 1, s - 1, memo) + dp(x - 1, s - 1, memo) + dp(x, s - 1, memo)) % MOD
            return memo[x, s]
        return dp(0, steps, {})
