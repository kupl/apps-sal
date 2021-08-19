class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        # dp[i][k] means the min job difficulty when we want to schedule the first i tasks during k days
        dp = [[float('inf')] * (d + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        # Init the above with padding
        for i in range(1, n + 1):
            for k in range(1, d + 1):
                max_difficulty = 0
                j = i - 1
                while j >= k - 1:
                    # print(max_difficulty)
                    max_difficulty = max(max_difficulty, jobDifficulty[j])
                    # print(dp)
                    dp[i][k] = min(dp[i][k], dp[j][k - 1] + max_difficulty)
                    j -= 1
        print(dp)
        return dp[n][d]
