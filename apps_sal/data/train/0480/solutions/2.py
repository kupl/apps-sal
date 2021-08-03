class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if steps is None or steps < 0 or not arrLen:
            return 0
        arrLen = min(arrLen, steps + 1)
        memo = [[0] * arrLen for _ in range(steps + 1)]
        memo[0][0] = 1
        for i in range(1, steps + 1):
            for j in range(arrLen):
                memo[i][j] += memo[i - 1][j]
                if j > 0:
                    memo[i][j] += memo[i - 1][j - 1]
                if j < arrLen - 1:
                    memo[i][j] += memo[i - 1][j + 1]
        return memo[steps][0] % (10 ** 9 + 7)
