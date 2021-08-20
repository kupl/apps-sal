class Solution:

    def palindromePartition(self, s: str, k: int) -> int:

        def min_change(s, i, j):
            a = 0
            while i < j:
                if s[i] != s[j]:
                    a += 1
                i += 1
                j -= 1
            return a
        cost = [[0 for j in range(len(s))] for i in range(len(s))]
        n = len(s)
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] != s[j]:
                    cost[i][j] = cost[i + 1][j - 1] + 1
                else:
                    cost[i][j] = cost[i + 1][j - 1]
        dp = [[float('inf') for j in range(n)] for i in range(k + 1)]
        for i in range(n):
            dp[1][i] = cost[0][i]
            for kk in range(2, k + 1):
                for j in range(i):
                    dp[kk][i] = min(dp[kk][i], dp[kk - 1][j] + cost[j + 1][i])
        return dp[-1][-1]
