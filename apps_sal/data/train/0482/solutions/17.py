class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        N = len(arr)
        dp = [[[0, i] for i in arr]]
        for l in range(1, N):
            dp.append([])
            for i in range(N - l):
                dp[l].append([sys.maxsize, 0])
                for x in range(i, i + l):
                    tmp = dp[x - i][i][0] + dp[i + l - x - 1][x + 1][0] + dp[x - i][i][1] * dp[i + l - x - 1][x + 1][1]
                    if tmp < dp[l][i][0]:
                        dp[l][i] = [tmp, max(dp[x - i][i][1], dp[i + l - x - 1][x + 1][1])]
        return dp[-1][0][0]
