class Solution:

    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        memo = {}

        def dp(i, j):
            if i == 0:
                return 1 if j == 0 else 0
            if (i, j) in memo:
                return memo[i, j]
            ans = dp(i - 1, j - 1) * (N - (j - 1))
            ans += dp(i - 1, j) * max(0, j - K)
            memo[i, j] = ans % (10 ** 9 + 7)
            return memo[i, j]
        return dp(L, N)
