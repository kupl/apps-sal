class Solution:

    def minDifficulty(self, difficulty: List[int], d: int) -> int:
        if d > len(difficulty):
            return -1
        n = len(difficulty)
        dp = [[float('inf')] * (n + 1) for _ in range(d + 1)]
        dp[0][0] = 0
        for i in range(d):
            for j in range(n):
                local = float('-inf')
                for k in range(j, -1, -1):
                    if k < i:
                        break
                    local = max(local, difficulty[k])
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], local + dp[i][k])
        return dp[d][n]
