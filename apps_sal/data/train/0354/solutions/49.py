class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0 for _ in range(7)] for _ in range(n + 1)]
        dp[1] = [0] + [1 for _ in range(1, 7)]
        mod = 10 ** 9 + 7
        for i in range(2, n + 1):
            for j in range(1, 7):
                for k in range(1, rollMax[j - 1] + 1):
                    if i - k > 0:
                        dp[i][j] += sum(dp[i - k]) - dp[i - k][j]
                    if i - k == 0:
                        dp[i][j] += 1
        return sum(dp[n]) % mod
