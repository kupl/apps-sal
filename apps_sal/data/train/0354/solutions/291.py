class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0] * 6 for _ in range(n + 1)]
        dp[1] = [1] * 6
        for i in range(2, n + 1):
            for j in range(6):
                dp[i][j] = sum((dp[i - 1][j] for j in range(6)))
                if i == rollMax[j] + 1:
                    dp[i][j] -= 1
                elif i > rollMax[j] + 1:
                    dp[i][j] -= sum((dp[i - rollMax[j] - 1][k] for k in range(6) if k != j))
        return sum(dp[-1]) % (10 ** 9 + 7)
