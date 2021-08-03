class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        memo = {}

        def dp(i, j):
            if i == 0:
                return j == 0
            if (i, j) in memo:
                return memo[i, j]
            memo[i, j] = dp(i - 1, j - 1) * (N - j + 1) + dp(i - 1, j) * max(j - K, 0)
            return memo[i, j]

        return dp(L, N) % (10**9 + 7)
