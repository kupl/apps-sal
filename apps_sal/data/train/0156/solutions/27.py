class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            dp[i + 1][0] = dp[i][0] + 1

        for i in range(n):
            dp[0][i + 1] = dp[0][i] + 1

        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j]) + 1

        ans = []

        i = m
        j = n
        while i > 0 or j > 0:
            if i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1 and str1[i - 1] == str2[j - 1]:
                i -= 1
                j -= 1
                ans.append(str1[i])
            elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
                i -= 1
                ans.append(str1[i])
            elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
                j -= 1
                ans.append(str2[j])
        return ''.join(ans[::-1])
