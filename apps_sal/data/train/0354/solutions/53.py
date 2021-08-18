from functools import lru_cache


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7

        @lru_cache
        def roll(i, j):
            if i == 0:
                return 1

            ans = 0
            for dice in range(6):
                if dice == j:
                    continue

                for k in range(1, min(rollMax[dice], i) + 1):
                    ans += roll(i - k, dice)
                    ans %= MOD
            return ans % MOD

        return roll(n, -1)
