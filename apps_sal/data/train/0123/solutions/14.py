class Solution:

    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        mod = 10 ** 9 + 7

        @lru_cache(None)
        def dp(l, n):
            if not l:
                return not n
            return dp(l - 1, n - 1) * (N - n + 1) + dp(l - 1, n) * max(n - K, 0)
        return dp(L, N) % mod
