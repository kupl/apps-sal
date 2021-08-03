class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        for i in range(1, n):
            if s.startswith(s[i:]):
                return s[i:]
        return ''


class Solution2:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if i == 0:
                        dp[i][j] = 1
                    elif dp[i - 1][j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
        max_len = 0
        for i in range(n):
            max_len = max(max_len, dp[i][n - 1])
        return s[-max_len:] if max_len else ''
