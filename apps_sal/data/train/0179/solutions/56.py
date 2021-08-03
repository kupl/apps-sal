class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        def calc(l):
            if l == 0:
                return 0
            elif l == 1:
                return 1
            elif l < 10:
                return 2
            elif l < 100:
                return 3
            return 4

        dp = [[float('inf')] * (k + 1) for _ in range(len(s) + 1)]

        for i in range(k + 1):
            dp[0][i] = 0

        for i in range(1, len(s) + 1):
            for j in range(0, k + 1):
                # print(\"{0} {1}\".format(i,j))
                if j > 0:
                    dp[i][j] = dp[i - 1][j - 1]

                rem, cnt = 0, 0
                for p in range(i, 0, -1):
                    if s[p - 1] == s[i - 1]:
                        cnt += 1
                    else:
                        rem += 1

                    if rem > j:
                        break

                    dp[i][j] = min(dp[i][j],
                                   dp[p - 1][j - rem] + calc(cnt))

        # for row in dp:
        #     print(row)

        return dp[len(s)][k]
