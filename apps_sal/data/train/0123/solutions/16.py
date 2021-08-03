class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        dp = [[0 for i in range(L + 1)] for j in range(N + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if i == j:
                    dp[i][j] = math.factorial(i)
                else:
                    dp[i][j] = dp[i - 1][j - 1] * i + dp[i][j - 1] * max((i - K), 0)
        print(dp)
        return dp[N][L] % (10**9 + 7)
