class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target > f * d:
            return 0

        @lru_cache(None)
        def dp(target, f, d):
            if target == 0 and d == 0:
                return 1
            if target <= 0:
                return 0
            count = 0
            for i in range(1, f + 1):
                count += dp(target - i, f, d - 1)
                count %= 10 ** 9 + 7
            return count
        return int(dp(target, f, d) % (10 ** 9 + 7))
