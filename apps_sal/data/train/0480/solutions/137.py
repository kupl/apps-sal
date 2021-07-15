from collections import defaultdict
def numWays(steps: int, arrLen: int) -> int:
    if steps is None or steps < 0 or not arrLen:
        return 0
    arrLen = min(arrLen, steps + 1)
    f = [[0] * arrLen for _ in range(steps + 1)]
    f[0][0] = 1
    for i in range(1, steps + 1):
        for j in range(min(arrLen, i+1)):
            f[i][j] += f[i - 1][j]
            if j > 0:
                f[i][j] += f[i - 1][j - 1]
            if j < arrLen - 1:
                f[i][j] += f[i - 1][j + 1]
    return f[steps][0] % (10 ** 9 + 7)
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        return numWays(steps,arrLen)

