class Solution:

    def stoneGameIII(self, stones: List[int]) -> str:
        n = len(stones)
        dp = [-math.inf] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            take = 0
            for j in range(i + 1, min(i + 3, n) + 1):
                take += stones[j - 1]
                dp[i] = max(dp[i], take - dp[j])
        return 'Alice' if dp[0] > 0 else 'Bob' if dp[0] < 0 else 'Tie'
