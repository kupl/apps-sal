class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        memo = {}

        def nw(i: int, k: int) -> int:
            if k == 0:
                return i == 0
            if k < 0 or i < 0 or i >= arrLen:
                return 0
            if (i, k) not in memo:
                memo[(i, k)] = (nw(i - 1, k - 1) + nw(i + 1, k - 1) + nw(i, k - 1)) % MOD
            return memo[(i, k)]

        return nw(0, steps)
