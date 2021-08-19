from functools import lru_cache


class Solution:

    def numWays(self, steps: int, n: int) -> int:
        MOD = 10 ** 9 + 7

        def calculate(pos, steps):
            nonlocal dp
            if pos < 0 or pos >= n:
                return 0
            if pos > steps:
                return 0
            if steps == pos:
                return 1
            steps -= 1
            if (pos + 1, steps) in dp:
                step1 = dp[pos + 1, steps]
            else:
                step1 = calculate(pos + 1, steps)
                dp[pos + 1, steps] = step1
            if (pos - 1, steps) in dp:
                step2 = dp[pos - 1, steps]
            else:
                step2 = calculate(pos - 1, steps)
                dp[pos - 1, steps] = step2
            if (pos, steps) in dp:
                step3 = dp[pos, steps]
            else:
                step3 = calculate(pos, steps)
                dp[pos, steps] = step3
            return (step1 + step2 + step3) % MOD
        dp = {}
        return calculate(0, steps)
