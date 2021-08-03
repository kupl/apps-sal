class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        maxPos = min(steps, arrLen)
        mod = 10**9 + 7
        f = [[0] * maxPos for _ in range(steps + 1)]
        f[1][0] = 1
        f[1][1] = 1
        for i in range(2, steps + 1):
            for j in range(maxPos):
                f[i][j] = f[i - 1][j]
                if j > 0:
                    f[i][j] = (f[i][j] + f[i - 1][j - 1]) % mod
                if j < maxPos - 1:
                    f[i][j] = (f[i][j] + f[i - 1][j + 1]) % mod
        return f[steps][0]
