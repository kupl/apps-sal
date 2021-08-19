class Solution:

    def numWays(self, steps: int, n: int) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def calculate(pos, steps):
            if pos < 0 or pos >= n:
                return 0
            if pos > steps:
                return 0
            if steps == pos:
                return 1
            steps -= 1
            return (calculate(pos + 1, steps) + calculate(pos - 1, steps) + calculate(pos, steps)) % MOD
        return calculate(0, steps)
