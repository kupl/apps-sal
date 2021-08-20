class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        (M, K) = (6, 15)
        dp = [[[0] * (K + 1) for _ in range(M + 1)] for _ in range(n + 1)]
        for i in range(1, M + 1):
            dp[1][i][1] = 1
        for i in range(2, n + 1):
            for j in range(1, M + 1):
                for m in range(1, M + 1):
                    if m != j:
                        dp[i][j][1] += sum((dp[i - 1][m][h] for h in range(1, rollMax[m - 1] + 1)))
                for k in range(1, K):
                    dp[i][j][k + 1] += dp[i - 1][j][k]
        ans = 0
        for m in range(1, M + 1):
            for k in range(1, rollMax[m - 1] + 1):
                ans += dp[-1][m][k]
        return ans % (10 ** 9 + 7)
