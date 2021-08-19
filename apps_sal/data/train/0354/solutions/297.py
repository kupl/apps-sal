class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        L = len(rollMax)
        N = n
        dp = [[0] * (L + 1) for _ in range(N + 1)]      # dp[roll][index]

        dp[0][L] = 1
        for i in range(L):
            dp[1][i] = 1
        dp[1][L] = L

        # roll a dice
        for i in range(2, N + 1):
            # for each faces
            for j in range(L):
                for k in range(1, rollMax[j] + 1):
                    if i - k < 0:
                        break
                    dp[i][j] += dp[i - k][L] - dp[i - k][j]
            # sum all rows
            dp[i][L] = sum(dp[i][:L])

        return dp[N][L] % (10**9 + 7)
