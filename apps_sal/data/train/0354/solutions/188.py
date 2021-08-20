MOD = 1000000007


class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0] * 6 for _ in range(n)]
        total = [0] * n
        for d in range(6):
            dp[0][d] = 1
        total[0] = sum((dp[0][d] for d in range(6)))
        for i in range(1, n):
            for d in range(6):
                if i < rollMax[d]:
                    dp[i][d] = total[i - 1]
                else:
                    dp[i][d] = sum((total[j] - dp[j][d] for j in range(i - rollMax[d], i))) % MOD
            total[i] = sum((dp[i][d] for d in range(6))) % MOD
        return total[n - 1]
