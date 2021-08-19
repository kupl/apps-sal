class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dp(dice, target):
            if dice == 0:
                return int(target == 0)
            elif target <= 0:
                return 0
            else:
                res = 0
                for x in range(1, f + 1):
                    res += dp(dice - 1, target - x)
                return res % MOD
        return dp(d, target)
