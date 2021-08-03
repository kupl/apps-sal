class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MODULO = 10**9 + 7

        n_num = len(rollMax)

        dp = [[0] * (n_num + 1) for _ in range(n + 1)]
        dp[0][-1] = 1

        dp[1] = [1 for _ in range(n_num + 1)]
        dp[1][-1] = n_num

        for i in range(2, n + 1):
            dp[i] = [(dp[i - 1][-1])] * (n_num + 1)
            for j in range(n_num):
                k = i - rollMax[j]
                if k > 0:
                    dp[i][j] -= (dp[k - 1][-1] - dp[k - 1][j])
                dp[i][j] = dp[i][j] % MODULO
            dp[i][-1] = sum(dp[i][:-1]) % MODULO

        return dp[-1][-1]
