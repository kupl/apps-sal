class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        kmax = 15
        kmod = pow(10, 9) + 7

        # dp[i][j][k]: # of sequences ends with k consecutive j after i rolls
        dp = [[[0] * (kmax + 1) for _ in range(6)] for _ in range(n + 1)]

        for j in range(6):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(6):
                for p in range(6):
                    for k in range(1, rollMax[p] + 1):
                        if p != j:
                            dp[i][j][1] = (dp[i][j][1] + dp[i - 1][p][k]) % kmod
                        elif k < rollMax[p]:
                            dp[i][j][k + 1] = (dp[i][j][k + 1] + dp[i - 1][p][k]) % kmod

        ans = 0
        for j in range(6):
            for k in range(1, rollMax[j] + 1):
                ans = (ans + dp[n][j][k]) % kmod

        return ans
