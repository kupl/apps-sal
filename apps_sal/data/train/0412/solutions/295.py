class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}

        def solve(dice, target):
            if target > dice * f:
                memo[dice, target] = 0
                return 0
            if dice == 0:
                return target == 0
            if target == 0:
                return 0
            if (dice, target) in memo:
                return memo[dice, target]
            ways = 0
            for num in range(1, f + 1):
                ways += solve(dice - 1, target - num)
            memo[dice, target] = ways
            return ways
        return solve(d, target) % (10 ** 9 + 7)
