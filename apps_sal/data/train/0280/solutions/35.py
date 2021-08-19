class Solution:

    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        self.cost = [[0 for _ in range(n)] for _ in range(n)]
        for l in range(2, n + 1):
            i = 0
            while i + l - 1 < n:
                j = i + l - 1
                self.cost[i][j] = self.cost[i + 1][j - 1] + (s[i] != s[j])
                i += 1
        self.dp = [[n for _ in range(k + 1)] for _ in range(n)]
        for i in range(n):
            self.dp[i][1] = self.cost[0][i]
            for K in range(2, k + 1):
                for j in range(i):
                    self.dp[i][K] = min(self.dp[i][K], self.dp[j][K - 1] + self.cost[j + 1][i])
        return self.dp[n - 1][k]
