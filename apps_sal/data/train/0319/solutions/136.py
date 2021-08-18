class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        n = len(stoneValue)
        dp = [-math.inf] * n
        for i in range(n - 1, -1, -1):
            take = 0
            for j in range(i, min(i + 3, n)):
                take += stoneValue[j]
                if j + 1 == n:
                    dp[i] = max(dp[i], take)
                else:
                    dp[i] = max(dp[i], take - dp[j + 1])
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] == 0:
            return 'Tie'
        else:
            return 'Bob'
