class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target > 900:
            return 0
        memo = {}

        def dfs(dice, t):
            if dice == 0 and t == 0:
                return 1
            if dice == 0 or t == 0:
                return 0
            if (dice, t) in memo:
                return memo[dice, t]
            count = 0
            for n in range(1, f + 1):
                count += dfs(dice - 1, t - n)
            memo[dice, t] = count % (10 ** 9 + 7)
            return memo[dice, t]
        return dfs(d, target)
