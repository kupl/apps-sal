class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d > target or d * f < target:
            return 0

        if f > target:
            f = target

        memo = [[0 for _ in range(target)] for _ in range(d)]

        for i in range(f):
            memo[0][i] = 1

        for i, row in enumerate(memo[1:]):
            for j, _2 in enumerate(row):
                if j - f < 0:
                    memo[i + 1][j] = sum(memo[i][0:j]) % 1000000007
                else:
                    memo[i + 1][j] = sum(memo[i][j - f:j]) % 1000000007

        return memo[-1][-1] % 1000000007
