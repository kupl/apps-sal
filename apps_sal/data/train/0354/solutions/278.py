class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0] * 7 for _ in range(n + 1)]
        ans = 1
        for i in range(1, n + 1):
            temp = 0
            for (j, r) in enumerate(rollMax):
                if i - r > 1:
                    dp[i][j] = ans - dp[i - r - 1][-1] + dp[i - r - 1][j]
                elif i - r == 1:
                    dp[i][j] = ans - 1
                else:
                    dp[i][j] = ans
                temp += dp[i][j]
            dp[i][-1] = temp
            ans = temp
        return temp % int(1000000000.0 + 7)
