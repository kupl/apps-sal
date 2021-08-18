

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        dp = [[0 for _ in range(7)] for i in range(n + 1)]
        kMod = 1e9 + 7

        for i in range(1, 7):
            dp[1][i] = 1

        for i in range(2, n + 1):

            for j in range(1, 7):

                k = i - rollMax[j - 1]

                dp[i][j] = sum(dp[i - 1])

                invalid = max(0, k) if k <= 1 else (sum(dp[k - 1]) - dp[k - 1][j])
                dp[i][j] = ((dp[i][j] - invalid) % kMod + kMod) % kMod

        return int(sum(dp[-1]) % (kMod))
