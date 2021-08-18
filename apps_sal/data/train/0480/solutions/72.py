class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mem = {}

        def helper(i, k, arrLen):
            if i == 0 and k == 0:
                return 1
            if (i, k) in mem:
                return mem[(i, k)]
            count = 0
            for x in [-1, 0, 1]:
                if i + x < 0 or i + x >= arrLen or k < 0:
                    continue
                count += helper(i + x, k - 1, arrLen)
            mem[(i, k)] = count
            return count
        return helper(0, steps, arrLen) % (10**9 + 7)
