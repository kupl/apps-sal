class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i, c in enumerate(s1):
            for j, d in enumerate(s2):
                dp[i + 1][j + 1] = 1 + dp[i][j] if c == d else max(dp[i + 1][j], dp[i][j + 1])
        i, j, stk = m - 1, n - 1, []
        while i >= 0 and j >= 0:
            if s1[i] == s2[j]:
                stk.append(s1[i])
                i -= 1
                j -= 1
            elif dp[i + 1][j] < dp[i][j + 1]:
                stk.append(s1[i])
                i -= 1
            else:
                stk.append(s2[j])
                j -= 1 
        return s1[: i + 1] + s2[: j + 1] + ''.join(reversed(stk))
