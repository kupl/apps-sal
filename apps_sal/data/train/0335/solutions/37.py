class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        if n == 0:
            return 0
        sum_ = sum(rods)
        dp = [[-1 for j in range(sum_ + 1)] for i in range(n + 1)]
        dp[0][0] = 0
        for i in range(n + 1):
            h = rods[i - 1]
            for j in range(sum_ - h + 1):
                if dp[i - 1][j] < 0:
                    continue
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
                dp[i][j + h] = max(dp[i][j + h], dp[i - 1][j])
                dp[i][abs(j - h)] = max(dp[i][abs(j - h)], dp[i - 1][j] + min(h, j))

        return dp[n][0]
