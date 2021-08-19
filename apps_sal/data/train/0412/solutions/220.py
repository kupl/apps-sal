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
                count %= (10**9 + 7)

            return count

        return int(dp(target, f, d) % (10**9 + 7))


# # ############
# f = 3
# ans = [1,1,2],[1,2,1],[2,1,1]
# count = 3
# dp(3, 4)
# d = 3
# target = 4
# i = 2
# -------
# dp(2, 2)
# d = 2
# target = 2
# i = 1
# ------
# dp(1, 1)
# d = 1
# target = 1
# i = 1
# ------
# dp(0, 0)
# d = 0
# target = 0
# ------
