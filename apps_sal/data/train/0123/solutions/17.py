class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        dp = [0 for _ in range(L + 1)]
        dp[0] = 1
        for i in range(1, N + 1):
            dp2 = [0 for _ in range(L + 1)]
            for j in range(1, L + 1):
                dp2[j] = dp[j - 1] * (N - i + 1)
                dp2[j] += dp2[j - 1] * max(i - K, 0)
            dp = dp2

        return dp[L] % (10**9 + 7)
