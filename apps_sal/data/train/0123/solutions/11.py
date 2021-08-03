class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        BIG = 10**9 + 7

        @lru_cache(None)
        def dp(r, n):
            if r == 0:
                return 1 if n == 0 else 0
            return (dp(r - 1, n - 1) * (N - (n - 1)) + dp(r - 1, n) * max(0, n - K)) % BIG

        return dp(L, N)
