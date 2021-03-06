class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[[0 for _ in range(max(rollMax) + 1)] for _ in range(7)] for _ in range(n + 1)]
        kMod = 1000000000.0 + 7
        for i in range(1, 7):
            dp[1][i][1] = 1
        for i in range(2, n + 1):
            for j in range(1, 7):
                for l in range(1, 7):
                    if l != j:
                        dp[i][j][1] += sum(dp[i - 1][l]) % kMod
                    else:
                        for k in range(1, rollMax[j - 1] + 1):
                            dp[i][j][k] += dp[i - 1][j][k - 1] % kMod
        temp = sum([sum(i) % kMod for i in dp[-1]])
        return int(temp % kMod)

    def dieSimulator_temp(self, n: int, rollMax: List[int]) -> int:
        dp = [[0 for _ in range(7)] for i in range(n + 1)]
        kMod = 1000000000.0 + 7
        for i in range(1, 7):
            dp[1][i] = 1
        for i in range(2, n + 1):
            for j in range(1, 7):
                k = i - rollMax[j - 1]
                dp[i][j] = sum(dp[i - 1])
                invalid = max(0, k) if k <= 1 else sum(dp[k - 1]) - dp[k - 1][j]
                dp[i][j] = ((dp[i][j] - invalid) % kMod + kMod) % kMod
        return int(sum(dp[-1]) % kMod)
