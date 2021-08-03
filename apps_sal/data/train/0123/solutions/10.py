class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        # 11:35
        # pick k+1 songs out of N Songs
        # k+1 factorial
        # you can pick a new song or old song from this k+1 => basically you got N options now

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
