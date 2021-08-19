from functools import lru_cache


class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        # Dynamic Programming
        # Let dp[i][j] be the number of playlists of length i that have exactly j unique songs.
        # Time  complexity: O(NL)
        # Space complexity: O(NL)
        @lru_cache(None)
        def dp(i, j):
            if i == 0:
                return +(j == 0)
            ans = dp(i - 1, j - 1) * (N - j + 1)
            ans += dp(i - 1, j) * max(j - K, 0)
            return ans % (10**9 + 7)

        return dp(L, N)
