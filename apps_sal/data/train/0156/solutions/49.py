class Solution:

    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        (m, n) = (len(s1), len(s2))
        dp = [[''] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + s1[i] if i > 0 and j > 0 else s1[i]
                elif i > 0 and j > 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
                elif i > 0:
                    dp[i][j] = dp[i - 1][j]
                elif j > 0:
                    dp[i][j] = dp[i][j - 1]
        (res, i, j) = ('', 0, 0)
        for ch in dp[-1][-1]:
            while i < len(s1) and s1[i] != ch:
                res += s1[i]
                i += 1
            while j < len(s2) and s2[j] != ch:
                res += s2[j]
                j += 1
            res += ch
            i += 1
            j += 1
        res += s1[i:] + s2[j:]
        return res
