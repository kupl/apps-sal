from functools import lru_cache


class Solution:
    def numPermsDISequence(self, S: str) -> int:
        MOD = 10 ** 9 + 7
        
        @lru_cache(None)
        def presum(n, last):
            if last == 0:
                return 0
            return DP(n, last - 1) + presum(n, last - 1)

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

