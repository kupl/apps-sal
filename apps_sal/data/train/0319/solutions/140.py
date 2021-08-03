
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 3)

        total = 0
        for i in range(n - 1, -1, -1):
            total += stoneValue[i]
            dp[i] = -float('inf')
            for k in range(1, 4, 1):
                dp[i] = max(total - dp[i + k], dp[i])

        oppo = total - dp[0]
        if dp[0] > oppo:
            return 'Alice'
        elif dp[0] < oppo:
            return 'Bob'
        return 'Tie'
