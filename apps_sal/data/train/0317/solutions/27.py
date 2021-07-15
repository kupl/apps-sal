from functools import lru_cache


class Solution:
    def numPermsDISequence(self, S: str) -> int:
        MOD = 10 ** 9 + 7
        
        def presum(n, last):
            return sum(
                DP(n, x)
                for x in range(last)
            )
        
        @lru_cache(None)
        def DP(n, last):
            if n == 0:
                return 1
            if S[n - 1] == 'D':
                return (presum(n - 1, n) - presum(n - 1, last)) % MOD
            else:
                return presum(n - 1, last) % MOD

        return sum(
            DP(len(S), i)
            for i in range(len(S) + 1)
        ) % MOD

