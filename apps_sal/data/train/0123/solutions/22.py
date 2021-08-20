class Solution:

    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:

        @lru_cache(None)
        def dp(i, j):
            if i == 0:
                return j == 0
            return (dp(i - 1, j) * max(0, j - K) + dp(i - 1, j - 1) * (N - j + 1)) % (10 ** 9 + 7)
        return dp(L, N)
