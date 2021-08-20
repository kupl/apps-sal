class Solution:

    def palindromePartition(self, s: str, k: int) -> int:
        l = len(s)

        def jbn(a):
            le = len(a)
            return sum((a[i] != a[le - 1 - i] for i in range(le // 2)))
        dp = [[0] * (l + 1) for _ in range(k + 1)]
        for j in range(1, l + 1):
            dp[1][j] = jbn(s[:j])
        for i in range(2, k + 1):
            for j in range(i + 1, l + 1):
                dp[i][j] = min((dp[i - 1][m] + jbn(s[m:j]) for m in range(i - 1, j)))
        return dp[k][l]
