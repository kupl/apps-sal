class Solution:
    def getLengthOfOptimalCompression(self, s, k):
        n = len(s)
        dp = [[9999] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(k + 1):
                cnt = 0
                del_ = 0
                for l in range(i, 0, -1):  # Keep s[i - 1], remove s[l - 1] if it's different char
                    if s[l - 1] == s[i - 1]:
                        cnt += 1
                    else:
                        del_ += 1
                    if j - del_ >= 0:
                        dp[i][j] = min(dp[i][j], dp[l - 1][j - del_] + 1 + (3 if cnt > 99 else 2 if cnt > 9 else 1 if cnt > 1 else 0))
                if j > 0:  # remove s[i - 1]
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

        return dp[n][k]
