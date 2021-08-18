class Solution:
    def minDifficulty(self, difficulty: List[int], d: int) -> int:
        if d > len(difficulty):
            return -1

        n = len(difficulty)
        dp = [float('inf')] * n + [0]

        for i in range(d):
            for j in range(n - 1, i - 1, -1):
                dp[j] = float('inf')
                local = float('-inf')
                for k in range(j, i - 1, -1):
                    local = max(local, difficulty[k])
                    dp[j] = min(dp[j], dp[k - 1] + local)

        return dp[-2]
