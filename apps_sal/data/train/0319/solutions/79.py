class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [0] * len(stoneValue)
        for i in range(len(stoneValue) - 1, -1, -1):
            ans = float('-inf')
            ans = max(ans, stoneValue[i] - (dp[i + 1] if i + 1 < len(stoneValue) else 0))
            if i + 1 < len(stoneValue):
                ans = max(ans, stoneValue[i] + stoneValue[i + 1] - (dp[i + 2] if i + 2 < len(stoneValue) else 0))
            if i + 2 < len(stoneValue):
                ans = max(ans, stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - (dp[i + 3] if i + 3 < len(stoneValue) else 0))
            dp[i] = ans
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'
