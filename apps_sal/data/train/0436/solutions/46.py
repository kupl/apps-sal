class Solution:
    def minDays(self, n: int) -> int:
        self.m = 10000
        self.dp = [0, 1] + [float('inf')] * (self.m - 1)
        for i in range(2, self.m + 1):
            v = []
            v.append(self.dp[i - 1])
            if i % 2 == 0:
                v.append(self.dp[i // 2])
            if i % 3 == 0:
                v.append(self.dp[i // 3])
            self.dp[i] = min(v) + 1

        def dfs(n):
            if n <= self.m:
                return self.dp[n]
            else:
                return 1 + min(n % 2 + dfs(n // 2), n % 3 + dfs(n // 3))
        return dfs(n)
