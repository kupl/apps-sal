class Solution:

    def stoneGameIII(self, stones: List[int]) -> str:
        n = len(stones)
        dp = [-math.inf for _ in range(n + 1)]
        dp[n] = 0
        prefix = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + stones[i - 1]
        for i in range(n - 1, -1, -1):
            for k in range(1, 4):
                if i + k > n:
                    break
                dp[i] = max(dp[i], sum(stones[i:i + k]) + prefix[-1] - prefix[i + k] - dp[i + k])
        if dp[0] * 2 > sum(stones):
            return 'Alice'
        elif dp[0] * 2 < sum(stones):
            return 'Bob'
        else:
            return 'Tie'
