class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [0] * 3
        for i in range(len(stoneValue) - 1, -1, -1):
            dp[i % 3] = max(sum(stoneValue[i:i + k]) - dp[(i + k) % 3] for k in (1, 2, 3))
        if dp[0] == 0:
            return 'Tie'
        elif dp[0] > 0:
            return 'Alice'
        else:
            return 'Bob'

