class Solution:
    def palindromePartition(self, s: str, k: int) -> int:

        n = len(s)
        s = '#' + s
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        def count(a, b):
            count = 0
            while a < b:
                if s[a] != s[b]:
                    count += 1
                a += 1
                b -= 1
            return count

        for i in range(1, n + 1):
            for t in range(1, min(i + 1, k + 1)):
                for j in range(t, i + 1):
                    dp[i][t] = min(dp[i][t], dp[j - 1][t - 1] + count(j, i))

        return dp[n][k]
