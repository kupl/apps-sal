class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        dp = [[0] * (N + 1) for _ in range(L + 1)]
        dp[0][0] = 1

        for i in range(1, L + 1):
            for j in range(1, N + 1):
                dp[i][j] = dp[i - 1][j - 1] * (N - j + 1) % (10**9 + 7)
                if j > K:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - K)) % (10**9 + 7)

        return dp[L][N]

        # T=O(NL) S=O(NL)
        memo = {}

        def DFS(i, j):
            if i == 0:
                return j == 0
            if (i, j) in memo:
                return memo[(i, j)]
            ans = DFS(i - 1, j - 1) * (N - j + 1)
            ans += DFS(i - 1, j) * max(j - K, 0)
            memo[(i, j)] = ans % (10**9 + 7)
            return memo[(i, j)]

        return DFS(L, N)
