class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        self.arrLen = arrLen

        @lru_cache(None)
        def dp(curr, steps):
            if steps:
                temp = 0
                for i in [curr - 1, curr, curr + 1]:
                    if 0 <= i < self.arrLen:
                        temp += dp(i, steps - 1)
                return temp
            else:
                return 1 if curr == 0 else 0
        return dp(0, steps) % (10 ** 9 + 7)
