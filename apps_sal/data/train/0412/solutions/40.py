class Solution:
    def __init__(self):
        self.dp = []

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # Initiate memoization array
        for dice in range(0, d + 1):
            self.dp.append([-1] * (target + 1))

        return self.rollDice(d, f, target) % (10 ** 9 + 7)

    def rollDice(self, d: int, f: int, target: int) -> int:
        if self.dp[d][target] != -1:
            return self.dp[d][target]

        if d == 1:
            if f >= target:
                return 1
            else:
                return 0

        self.dp[d][target] = 0
        for nextRoll in range(1, f + 1):
            if target - nextRoll > 0:
                self.dp[d][target] += self.rollDice(d - 1, f, target - nextRoll)

        return self.dp[d][target]
