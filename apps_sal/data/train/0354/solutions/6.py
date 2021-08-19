from collections import defaultdict


class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0] * 7 for _ in range(n + 1)]
        prev = defaultdict(int)
        for i in range(1, 7):
            dp[1][i] = 1
            prev[i, 1] = 1
        for i in range(2, n + 1):
            new = defaultdict(int)
            for j in range(1, 7):
                new[j, 1] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5] + dp[i - 1][6] - dp[i - 1][j]
                dp[i][j] += new[j, 1]
                max_len = min(15, rollMax[j - 1])
                for k in range(1, max_len):
                    new[j, k + 1] = prev[j, k]
                    dp[i][j] += new[j, k + 1]
            prev = new
        count = 0
        for i in range(1, 7):
            count += dp[n][i]
        return count % 1000000007
