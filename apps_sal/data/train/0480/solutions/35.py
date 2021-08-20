class Solution:

    def __init__(self):
        self.dp = {}

    def numWays(self, steps: int, arrLen: int, ptr: int = 0) -> int:
        return self.numWays_dp(steps, min(arrLen, steps + 1), ptr) % (10 ** 9 + 7)

    def numWays_dp(self, steps: int, arrLen: int, ptr: int = 0) -> int:
        if ptr >= arrLen:
            return 0
        if ptr < 0:
            return 0
        if steps == 0:
            if ptr == 0:
                return 1
            else:
                return 0
        if (ptr, steps) in self.dp:
            return self.dp[ptr, steps]
        left_ways = self.numWays(steps - 1, arrLen, ptr - 1)
        middle_ways = self.numWays(steps - 1, arrLen, ptr)
        right_ways = self.numWays(steps - 1, arrLen, ptr + 1)
        total_ways = left_ways + middle_ways + right_ways
        self.dp[ptr, steps] = total_ways
        return total_ways
