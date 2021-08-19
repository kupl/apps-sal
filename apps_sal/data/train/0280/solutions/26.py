class Solution:

    def palindromePartition(self, s: str, k: int):
        cost = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    cost[i][j] = cost[i + 1][j - 1]
                else:
                    cost[i][j] = cost[i + 1][j - 1] + 1
        dp = [[float('inf')] * k for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][0] = cost[0][i]
            for m in range(1, k):
                for j in range(i):
                    dp[i][m] = min(dp[i][m], dp[j][m - 1] + cost[j + 1][i])
        return dp[-1][-1]
