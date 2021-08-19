MOD = 1000000007


class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0] * 6 for _ in range(n)]
        for d in range(6):
            dp[0][d] = 1
        for i in range(1, n):
            for d in range(6):
                if i < rollMax[d]:
                    dp[i][d] = sum((dp[i - 1][x] for x in range(6))) % MOD
                else:
                    dp[i][d] = sum((dp[j][x] for j in range(i - rollMax[d], i) for x in range(6) if x != d)) % MOD
        return sum((dp[n - 1][d] for d in range(6))) % MOD
