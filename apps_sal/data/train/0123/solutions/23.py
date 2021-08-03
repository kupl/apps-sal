class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:

        dp = [[0 for n in range(N + 1)] for l in range(L + 1)]
        dp[0][0] = 1
        for l in range(1, L + 1):
            for n in range(1, N + 1):
                dp[l][n] += dp[l - 1][n - 1] * (N - n + 1)
                dp[l][n] += dp[l - 1][n] * max(n - K, 0)
                dp[l][n] = dp[l][n] % (10 ** 9 + 7)
        return dp[L][N]
