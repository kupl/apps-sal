class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0 for _ in range(rollMax[i])] for i in range(6)]
        for i in range(6):
            dp[i][0] = 1
        for i in range(n - 1):
            ndp = [[0 for _ in range(rollMax[w])] for w in range(6)]
            roll_sum = [sum(i) for i in dp]
            total = sum(roll_sum)
            for j in range(6):
                ndp[j][0] = total - roll_sum[j]
                for k in range(1, rollMax[j]):
                    ndp[j][k] += dp[j][k - 1]
            dp = ndp
        return sum(sum(i) for i in dp) % (10**9 + 7)
