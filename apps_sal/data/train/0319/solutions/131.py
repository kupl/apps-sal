class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [-2**31] * n  # max diff points Alice can win over Bob
        for i in range(n - 1, -1, -1):
            take = 0
            for j in range(i, min(i + 3, n)):
                take += stoneValue[j]
                dp[i] = max(dp[i], take - (dp[j + 1] if j + 1 < n else 0))

        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'
