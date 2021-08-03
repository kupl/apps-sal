class Solution:
    base = 10**9 + 7

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[1] * rollMax[i] for i in range(6)]

        for m in range(1, n):
            s = sum(dp[k][-1] for k in range(6))
            zero = [s - dp[k][-1] for k in range(6)]

            for i in range(6):
                for j in range(rollMax[i] - 1, 0, -1):
                    dp[i][j] = (zero[i] + dp[i][j - 1]) % self.base
                dp[i][0] = zero[i] % self.base

        return sum(dp[i][-1] for i in range(6)) % self.base
