class Solution:
    def palindromePartition(self, s: str, K: int) -> int:
        n = len(s)
        dp = [[101 for k in range(K + 1)] for i in range(n)]
        num = [[0 for j in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(i):
                num[j][i] = self.helper(s[j:i + 1])

        for i in range(n):
            dp[i][1] = num[0][i]

        for k in range(2, K + 1):
            for i in range(k - 1, n):
                for j in range(k - 2, i):
                    dp[i][k] = min(dp[i][k], dp[j][k - 1] + num[j + 1][i])
        return dp[n - 1][K]

    def helper(self, s):
        l, r = 0, len(s) - 1
        count = 0
        while l < r:
            if s[l] != s[r]:
                count += 1
            l += 1
            r -= 1
        return count
