class Solution:
    import math
    from functools import lru_cache

    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        MOD = 1000000007

        @lru_cache(maxsize=None)
        def rec(n, l):
            if l < n or n <= K:
                return 0
            elif l == n:
                return math.factorial(n) % MOD
            return (n * rec(n - 1, l - 1) + (n - K) * rec(n, l - 1)) % MOD

        return rec(N, L)
