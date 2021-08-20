class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[[0] * (max(rollMax) + 1) for _ in range(6)] for _ in range(2)]
        for i in range(6):
            dp[0][i][1] = 1
        mod = 1000000007
        for i in range(n - 1):
            idx = i % 2
            dp[1 - idx] = [[0] * (max(rollMax) + 1) for _ in range(6)]
            for d in range(6):
                for pre in range(6):
                    if pre == d:
                        for cnt in range(rollMax[pre]):
                            dp[1 - idx][d][cnt + 1] += dp[idx][pre][cnt] % mod
                    else:
                        for cnt in range(rollMax[pre] + 1):
                            dp[1 - idx][d][1] += dp[idx][pre][cnt] % mod
        return sum([sum(x) for x in dp[1 - n % 2]]) % mod
