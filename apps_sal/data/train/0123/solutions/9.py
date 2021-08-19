class Solution:

    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        dp = [1] * (L - N + 1)
        for p in range(2, N - K + 1):
            for i in range(1, L - N + 1):
                dp[i] += dp[i - 1] * p
        ans = dp[-1]
        for k in range(2, N + 1):
            ans *= k
        return ans % (10 ** 9 + 7)
