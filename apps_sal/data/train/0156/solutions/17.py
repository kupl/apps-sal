class Solution:
    def shortestCommonSupersequence(self, a: str, b: str) -> str:
        n, m = len(a), len(b)

        dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]
        def TD(a, b, n, m):
            if dp[n][m] != -1:
                return dp[n][m]
            if n == 0 or m == 0:
                return 0
            if a[n - 1] == b[m - 1]:
                dp[n][m] = 1 + TD(a, b, n - 1, m - 1)
                return dp[n][m]
            dp[n][m] = max(TD(a, b, n - 1, m), TD(a, b, n, m - 1))
            return dp[n][m]
        idx = TD(a, b, n, m)
        lcs = ''
        i = n
        j = m
        while i > 0 and j > 0:
            if a[i - 1] == b[j - 1]:
                lcs+=a[i-1]
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j-1]:
                lcs+=a[i-1]
                i -= 1
            else:
                lcs+=b[j-1]
                j -= 1
        while i > 0:
            lcs += a[i - 1]
            i -= 1
        while j > 0:
            lcs += b[j - 1]
            j -= 1
        lcs = lcs[::-1]
        return lcs
