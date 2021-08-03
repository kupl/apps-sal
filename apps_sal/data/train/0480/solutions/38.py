class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(arrLen, steps + 1)
        f = [[0] * arrLen for _ in range(steps + 1)]
        f[0][0] = 1
        for i in range(1, steps + 1):
            for j in range(arrLen):
                for k in [-1, 0, 1]:
                    if 0 <= j - k < arrLen:
                        f[i][j] += f[i - 1][j - k]
        return f[steps][0] % (10**9 + 7)
