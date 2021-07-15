class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * (L + 1) for _ in range(N + 1)]
        
        for i in range(1, N + 1):
            for j in range(i, L + 1):
                if i == K + 1:# or i == j:
                    dp[i][j] = math.factorial(i)
                else:
                    dp[i][j] = dp[i - 1][j - 1] * i
                    if j > i:
                        dp[i][j] += dp[i][j - 1] * (i - K)
                dp[i][j] %= mod
        # print(dp)
        return dp[N][L]

