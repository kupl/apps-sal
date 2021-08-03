class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        m = max(rollMax)
        dp = [[[1] * m for _ in range(len(rollMax))] for _ in range(n)]
        dp[0] = [[1] + [0] * (m - 1) for _ in range(len(rollMax))]
        MOD = 1e9 + 7
        sumPrev = [1] * len(rollMax)
        for i in range(1, n):
            tempSumPrev = [0] * len(rollMax)
            totalSumPrev = 0
            for p in sumPrev:
                totalSumPrev = (totalSumPrev + p) % MOD
            for j in range(len(rollMax)):
                dp[i][j][0] = totalSumPrev - sumPrev[j]
                s = dp[i][j][0] % MOD
                for k in range(1, rollMax[j]):
                    dp[i][j][k] = dp[i - 1][j][k - 1]
                    s = (s + dp[i][j][k]) % MOD
                tempSumPrev[j] = s
            sumPrev = tempSumPrev
        return int(sum(sumPrev) % MOD)
