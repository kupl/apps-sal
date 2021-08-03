class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        @lru_cache(None)
        def nw(pos, left):

            if pos < 0:
                return 0

            if pos >= arrLen:
                return 0

            if left == 0 and pos == 0:
                return 1

            if left == 0 and pos != 0:
                return 0

            res = nw(pos + 1, left - 1)
            res += nw(pos - 1, left - 1)
            res += nw(pos, left - 1)

            return res

        res = nw(0, steps)

        return res % 1000000007
