class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(arrLen, steps)
        r = [[0] * arrLen for _ in range(steps)]
        r[0][0] = 1
        r[0][1] = 1
        mod = 10 ** 9 + 7
        for t in range(steps):
            for i in range(arrLen):
                r[t][i] += r[t - 1][i] + (r[t - 1][i - 1] if i > 0 else 0) + (r[t - 1][i + 1] if i < arrLen - 1 else 0)
                r[t][i] = r[t][i] % mod
        return r[t][0]
