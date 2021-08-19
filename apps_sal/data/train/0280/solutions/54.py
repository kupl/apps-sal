class Solution:

    def palindromePartition(self, s: str, k: int) -> int:

        def count(s):
            l = len(s)
            c = 0
            for i in range(int(l // 2)):
                if s[i] != s[l - 1 - i]:
                    c += 1
            return c
        s = '#' + s
        n = len(s)
        dp = [[float('inf')] * (k + 1) for _ in range(n)]
        dp[0][0] = 0
        for i in range(1, n):
            for j in range(1, k + 1):
                for m in range(j, i + 1):
                    dp[i][j] = min(dp[i][j], dp[m - 1][j - 1] + count(s[m:i + 1]))
        return dp[-1][-1]
