class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        M = 10 ** 9 + 7

        @lru_cache(None)
        def help(s, i):
            if s == 1:
                return 1 if i <= min(1, arrLen - 1) else 0
            out = help(s - 1, i)
            if i > 0:
                out += help(s - 1, i - 1)
            if i < arrLen - 1:
                out += help(s - 1, i + 1)
            return out % M
        return help(steps, 0)
