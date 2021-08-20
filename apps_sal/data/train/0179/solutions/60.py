def dlen(n):
    ans = 0
    while n > 0:
        ans += 1
        n //= 10
    return ans


class Solution:

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[float('inf') for _ in range(k + 1)] for _ in range(n + 1)]
        for j in range(k + 1):
            dp[0][j] = 0
        for i in range(1, n + 1):
            for j in range(k + 1):
                if j > 0:
                    dp[i][j] = dp[i - 1][j - 1]
                removed = 0
                count = 0
                for p in range(i, 0, -1):
                    if s[i - 1] == s[p - 1]:
                        count += 1
                    else:
                        removed += 1
                    if removed > j:
                        break
                    digit_len = 0 if count == 1 else dlen(count)
                    dp[i][j] = min(dp[i][j], dp[p - 1][j - removed] + 1 + digit_len)
        return dp[n][k]
