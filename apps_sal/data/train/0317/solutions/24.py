from functools import lru_cache


class Solution:
    def numPermsDISequence(self, S: str) -> int:
        MOD = 10 ** 9 + 7
        
        @lru_cache(None)
        def DP(n, last):
            if n == 0:
                return 1
            if S[n - 1] == 'D':
                return sum(
                    DP(n - 1, x - 1)
                    for x in range(last + 1, n + 1)
                ) % MOD
            else:
                return sum(
                    DP(n - 1, x)
                    for x in range(last)
                ) % MOD

        return sum(
            DP(len(S), i)
            for i in range(len(S) + 1)
        ) % MOD

