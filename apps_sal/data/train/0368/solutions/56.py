class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        dp = [[-1000000000.0] * n for i in range(n)]
        for i in range(n):
            for j in range(i + 1):
                dp[i][j] = max((dp[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0) + satisfaction[i] * (j + 1), dp[i - 1][j])
        ret = max(dp[-1])
        return ret if ret > 0 else 0
