class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}  # num of ways for combo of [# of rolls, target]

        def rollDice(d, target):
            if target < 0 or target > f * d:  # def 0 way
                memo[d, target] = 0
                return 0
            if d == 0:  # base case
                return 0 if target > 0 else 1
            if (d, target) in memo:  # if already computed
                return memo[d, target]
            total = 0  # actual computation
            for num in range(1, f + 1):
                total += rollDice(d - 1, target - num)  # dp based on previous roll
            memo[d, target] = total
            return total

        return rollDice(d, target) % (10**9 + 7)

    # for each roll, f doesn't change, dp[d, target] = dp[d-1, target-1] + dp[d-1, target-2] + ... + dp[d-1, target-f]. That is, cur total # of steps is sum of total # of steps of all possible last steps (determined by # of faces last dice has)
    # base case is when d is 0 (no roll left), target is 0, there is one way. If target > 0 and d is 0, there is no way.
    # bcs for each layer we have, the num of operations for the same d value is timed by f, there's a lot of repetition value there. Therefore we use memoization
