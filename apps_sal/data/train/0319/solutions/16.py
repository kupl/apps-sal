class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [0] * (len(stoneValue) + 1)
        for i in range(len(stoneValue) - 1, -1, -1):
            take = 0
            dp[i] = -float('inf')
            for k in range(3):
                if i + k >= len(stoneValue):
                    continue
                take += stoneValue[i + k]
                dp[i] = max(dp[i], take - dp[i + k + 1])
        if dp[0] < 0:
            return 'Bob'
        if dp[0] > 0:
            return 'Alice'
        return 'Tie'
