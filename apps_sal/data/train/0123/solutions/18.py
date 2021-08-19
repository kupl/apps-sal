import math


class Solution:

    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0 for _ in range(L + 1)] for _ in range(N + 1)]
        dp[0][0] = 1
        for i in range(1, N + 1):
            for j in range(1, L + 1):
                dp[i][j] = dp[i - 1][j - 1] * (N - i + 1) % mod
                dp[i][j] += dp[i][j - 1] * max(i - K, 0) % mod
        return dp[-1][-1] % mod
