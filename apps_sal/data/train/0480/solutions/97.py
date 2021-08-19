class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:

        @lru_cache(None)
        def helper(i, steps):
            if steps == 0:
                return i == 0
            elif steps < i or steps + i < 0:
                return 0
            else:
                result = helper(i, steps - 1)
                if i < arrLen - 1:
                    result += helper(i + 1, steps - 1)
                if i > 0:
                    result += helper(i - 1, steps - 1)
                return result % 1000000007
        mod = 1000000007
        return helper(0, steps)
