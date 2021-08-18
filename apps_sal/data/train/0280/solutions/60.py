class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[0 for j in range(k)] for i in range(n)]
        memo = {}

        def cost(i, j):
            if memo.get((i, j)):
                return memo[(i, j)]
            c = 0
            while i < j:
                if s[i] != s[j]:
                    c += 1
                i += 1
                j -= 1
            memo[(i, j)] = c
            return c

        for i in range(n):
            for j in range(k):
                if j > i:
                    break
                if j == 0:
                    dp[i][j] = cost(0, i)
                else:
                    dp[i][j] = min([dp[m][j - 1] + cost(m + 1, i) for m in range(i) if j - 1 <= m])
        return dp[n - 1][k - 1]
