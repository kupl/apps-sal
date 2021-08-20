class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}

        def rollDice(d, target):
            if target < 0 or target > f * d:
                memo[d, target] = 0
                return 0
            if d == 0:
                return 0 if target > 0 else 1
            if (d, target) in memo:
                return memo[d, target]
            total = 0
            for num in range(1, f + 1):
                total += rollDice(d - 1, target - num)
            memo[d, target] = total
            return total
        return rollDice(d, target) % (10 ** 9 + 7)
