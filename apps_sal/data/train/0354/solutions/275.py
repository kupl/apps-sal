class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[1] * 6 for _ in range(n)]
        for i in range(1, n):
            for j in range(6):
                dp[i][j] = sum(dp[i - 1])
                if i == rollMax[j]:
                    dp[i][j] -= 1
                if i > rollMax[j]:
                    for k in range(6):
                        if k != j:
                            dp[i][j] -= dp[i - 1 - rollMax[j]][k]
        return sum(dp[-1]) % (10 ** 9 + 7)
