class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        if steps == 0:
            return 0
        if arrLen == 1:
            return 1
        start = [1, 1] + [0] * (min(steps, arrLen) - 2)
        return self.numWaysHelper(steps - 1, start)

    def numWaysHelper(self, steps, start):
        if steps == 0:
            return start[0] % (10 ** 9 + 7)
        n = [0] * len(start)
        n[0] = start[0] + start[1]
        n[len(start) - 1] = start[len(start) - 1] + start[len(start) - 2]
        for i in range(1, len(start) - 1):
            n[i] = start[i - 1] + start[i] + start[i + 1]
        return self.numWaysHelper(steps - 1, n)
