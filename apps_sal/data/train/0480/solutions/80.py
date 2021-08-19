class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        (r, memo) = (min(arrLen, steps // 2 + 1), [0, 1])
        for t in range(steps):
            memo[1:] = [sum(memo[i - 1:i + 2]) for i in range(1, min(r + 1, t + 3))]
        return memo[1] % (10 ** 9 + 7)
