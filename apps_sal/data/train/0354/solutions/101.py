class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # dynamic programming
        # dp[i][j][k] # at pos i, we end with j, and the number of continuous of j at the end is k

        dp = [[[0 for k in range(rollMax[j] + 1)] for j in range(6)] for _ in range(n)]

        for j in range(6):
            dp[0][j][1] = 1

        for i in range(n):
            for j in range(6):
                for k in range(1, rollMax[j] + 1):
                    dp[i][j][k] += dp[i - 1][j][k - 1]

                for otherj in range(6):
                    if otherj != j:
                        for k in range(1, rollMax[otherj] + 1):
                            dp[i][j][1] += dp[i - 1][otherj][k]
        # print(\"dp=\", dp)
        return sum([sum(x) % (10**9 + 7) for x in dp[-1]]) % (10**9 + 7)
