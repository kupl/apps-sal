class Solution:

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        cp = s[:]
        dp = [[n + 1] * (k + 2) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for t in range(k + 1):
                dp[i][t + 1] = min(dp[i - 1][t], dp[i][t + 1])
                cnt = 0
                delete = 0
                for l in range(i, n + 1):
                    if cp[i - 1] == cp[l - 1]:
                        cnt += 1
                    else:
                        delete += 1
                    if t + delete <= k:
                        leng = dp[i - 1][t] + 1
                        if cnt >= 100:
                            leng += 3
                        elif cnt >= 10:
                            leng += 2
                        elif cnt >= 2:
                            leng += 1
                        else:
                            leng += 0
                        dp[l][t + delete] = min(dp[l][t + delete], leng)
                    else:
                        break
        return dp[n][k]
