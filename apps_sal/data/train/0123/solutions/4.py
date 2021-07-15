class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        dp = [[0] * (N + 1) for _ in range(L + 1)]
        dp[0][0] = 1
        for i in range(1, L + 1):
            for j in range(1, N + 1):
                dp[i][j] = dp[i - 1][j - 1] * (N - j + 1) #play new song
                if j > K: #play old song
                    dp[i][j] += dp[i - 1][j] * (j - K)
        return dp[-1][-1]%(10 ** 9 + 7)
                      
                

