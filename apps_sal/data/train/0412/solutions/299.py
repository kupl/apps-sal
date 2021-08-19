class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dp(dice, target):
            # number of ways to form target with `dice` remaining
            if target == 0:
                return int(dice == 0)
            elif target < 0 or dice <= 0:
                return 0
            else:  # target >= 0 and dice >= 0
                res = 0
                for x in range(1, f + 1):
                    res += dp(dice - 1, target - x)
                return res % MOD

        return dp(d, target)
