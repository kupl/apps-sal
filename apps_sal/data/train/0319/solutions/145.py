class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        p = [0] * n
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                p[i] = stoneValue[i]
            else:
                p[i] = stoneValue[i] + p[i + 1]
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = p[i] - min(dp[i + 1:i + 4])
        if dp[0] * 2 == p[0]:
            return 'Tie'
        elif dp[0] * 2 > p[0]:
            return 'Alice'
        else:
            return 'Bob'
