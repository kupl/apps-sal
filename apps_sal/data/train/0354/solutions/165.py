class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        max_num = max(rollMax)
        dp = [[[0] * (max_num + 1) for _ in range(6)] for _ in range(n + 1)]
        for j in range(6):
            dp[1][j][1] = 1
        for i in range(2, n + 1):
            for j in range(6):
                for p in range(6):
                    for k in range(1, max_num + 1):
                        if p != j:
                            dp[i][j][1] = (dp[i][j][1] + dp[i - 1][p][k]) % (10**9 + 7)
                        elif k < rollMax[p]:
                            dp[i][j][k + 1] = (dp[i][j][k + 1] + dp[i - 1][p][k]) % (10**9 + 7)
        ans = 0
        for j in range(6):
            for k in range(1, max_num + 1):
                ans = (ans + dp[n][j][k]) % (10**9 + 7)
        return ans
