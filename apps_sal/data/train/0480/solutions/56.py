class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        def count(pos, i):
            if i == steps:
                return pos == 0

            if (pos, i) in memo:
                return memo[(pos, i)]
            res = 0
            if pos > 0:
                res += count(pos - 1, i + 1)
                res %= mod
            if pos < arrLen - 1:
                res += count(pos + 1, i + 1)
                res %= mod
            res %= mod
            res += count(pos, i + 1)
            res %= mod

            memo[(pos, i)] = res
            return res

        mod = 10**9 + 7
        memo = {}
        return count(0, 0)
