class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * (n + 1) for _ in range(7)]
        for j in range(1, n + 1):
            tot = sum(dp[k][j - 1] for k in range(1, 7))
            for i in range(1, 7):
                if j == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = tot
                    if j > rollMax[i - 1] + 1:
                        dp[i][j] -= sum(dp[k][j - rollMax[i - 1] - 1] for k in range(1, 7) if k != i) - mod
                    elif j == rollMax[i - 1] + 1:
                        dp[i][j] -= 1
                    dp[i][j] %= mod
        # print(dp)
        return sum(dp[k][n] for k in range(1, 7)) % mod
