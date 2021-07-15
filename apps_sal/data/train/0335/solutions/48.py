class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        m = len(rods)
        total = sum(rods)
        dp = [[-1] * (5001) for _ in range(m + 1)]
        dp[0][0] = 0
        # dp[n][i]: means max common height we can achieve of using the first n elements that two
        # piles have the hight difference of i
        for i in range(1, m + 1):
            h = rods[i - 1]
            for j in range(5001 - h):
                if dp[i - 1][j] < 0:
                    continue
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
                dp[i][j + h] = max(dp[i - 1][j], dp[i][j + h])
                dp[i][abs(j - h)] = max(dp[i][abs(j - h)], dp[i - 1][j] + min(h, j))
        
        return dp[m][0]
