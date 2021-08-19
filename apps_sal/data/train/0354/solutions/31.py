class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[] for i in range(6)]
        new_dp = [[] for i in range(6)]
        for i in range(6):
            dp[i].append(1)
            for j in range(1, rollMax[i]):
                dp[i].append(0)
            new_dp[i] = [0 for i in range(rollMax[i])]
        for r in range(1, n):
            for i in range(6):
                new_dp[i][0] = sum([sum(dp[j]) if j != i else 0 for j in range(6)])
                for j in range(1, rollMax[i]):
                    new_dp[i][j] = dp[i][j - 1]
            (dp, new_dp) = (new_dp, dp)
        return sum([sum(x) for x in dp]) % (10 ** 9 + 7)
