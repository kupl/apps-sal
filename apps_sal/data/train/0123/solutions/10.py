class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:

        mod = 10**9 + 7

        @lru_cache(None)
        def helper(i, notplayed):
            nonlocal mod
            if i == L + 1:
                return 0 if notplayed != 0 else 1
            ans = (max((N - notplayed) - K, 0) * helper(i + 1, notplayed)) % mod
            if notplayed != 0:
                ans += (notplayed) * helper(i + 1, notplayed - 1)
            return ans % mod
        return helper(1, N)
