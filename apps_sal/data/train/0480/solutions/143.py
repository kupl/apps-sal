class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = [defaultdict(int) for _ in range(steps + 1)]

        dp[0][0] += 1
        dp[1][1] += 1
        dp[1][0] += 1

        modulo = pow(10, 9) + 7

        for i in range(2, steps + 1):
            for j in dp[i - 1].keys():
                remain = j - (steps - i)
                if j < 0:
                    break
                if j + 1 < arrLen:
                    dp[i][j + 1] += dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j - 1] += dp[i - 1][j]
                dp[i][j] += dp[i - 1][j]

        return dp[steps][0] % modulo
