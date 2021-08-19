class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(steps + 1, arrLen)
        num = [0 for i in range(arrLen)]
        num[0] = 1
        modulo = 10 ** 9 + 7
        for i in range(steps):
            newnum = [num[i] for i in range(arrLen)]
            for i in range(arrLen):
                if i > 0:
                    newnum[i] += num[i - 1]
                if i < arrLen - 1:
                    newnum[i] += num[i + 1]
                if newnum[i] > modulo:
                    newnum[i] %= modulo
            num = newnum
        return num[0]
