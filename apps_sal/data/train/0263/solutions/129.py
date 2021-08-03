class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = int(1e9 + 7)
        adj = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [0, 1, 7],
            [2, 6],
            [1, 3],
            [2, 4],
        ]
        dp = [[0] * 10 for _ in range(n + 1)]
        dp[1] = [1] * 10
        for i in range(2, n + 1):
            for j in range(10):
                for child in adj[j]:
                    dp[i][j] += dp[i - 1][child]
                    dp[i][j] %= MOD
        ans = 0
        for v in dp[n]:
            ans += v
            ans %= MOD
        return ans
