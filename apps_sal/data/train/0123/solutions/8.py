class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        dp = [[0 for _ in range(N + 1)] for _ in range(L + 1)]
        dp[0][0] = 1
        mod = 10**9 + 7
        for i in range(1, L + 1):
            for j in range(1, N + 1):
                dp[i][j] = dp[i - 1][j - 1] * (N - j + 1)
                if j > K:
                    dp[i][j] += dp[i - 1][j] * (j - K)
                dp[i][j] %= mod

        return dp[L][N]
