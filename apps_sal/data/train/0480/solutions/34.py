class Solution:

    def __init__(self):
        self.mnem = {}

    def numWays(self, steps: int, arrLen: int) -> int:

        def dp(pos, steps):
            if (pos, steps) in self.mnem:
                return self.mnem[pos, steps]
            if steps == 0:
                return 1 if pos == 0 else 0
            if pos < 0:
                return 0
            if pos >= arrLen:
                return 0
            result = dp(pos + 1, steps - 1) + dp(pos - 1, steps - 1) + dp(pos, steps - 1)
            self.mnem[pos, steps] = result
            return result
        return dp(0, steps) % (10 ** 9 + 7)
