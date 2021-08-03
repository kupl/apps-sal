class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        for i in range(len(rollMax)):
            rollMax[i] = min(rollMax[i], n)
        dp = []
        max_roll = max(rollMax) + 1
        for k in range(n + 1):
            dp.append([])
            for i in range(6):
                dp[-1].append([])
                for j in range(max_roll):
                    if k == 1 and j > 0:
                        dp[-1][-1].append(1)
                    else:
                        dp[-1][-1].append(0)

        MOD = (10 ** 9) + 7
        for k in range(1, n + 1):
            for prev_roll in range(6):
                for cur_roll in range(6):
                    for j in range(1, max_roll):
                        if prev_roll == cur_roll:
                            dp[k][prev_roll][j] += dp[k - 1][prev_roll][j - 1]
                        else:
                            dp[k][prev_roll][j] += dp[k - 1][cur_roll][rollMax[cur_roll]]
        ans = 0
        for i in range(6):
            ans += dp[n][i][rollMax[i]]
        return ans % MOD
