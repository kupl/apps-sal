class Solution:

    def mergeStones(self, stones: List[int], K: int) -> int:
        (dp, N, Sum, H) = ({}, len(stones), {-1: 0}, {})
        for i in range(N):
            (j, dp[i], H[i], Sum[i]) = (i, {}, {}, Sum[i - 1] + stones[i])
            while j > -1:
                H[i][j] = (i - j + 1) % (K - 1) + (K - 1) * (1 // (1 + (i - j + 1) % (K - 1)))
                if i - j < K - 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][i] + dp[i - 1][j]
                    for k in range(j + 1, i + 1):
                        if H[i][k] + H[k - 1][j] == H[i][j] or H[i][k] + H[k - 1][j] == K:
                            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k - 1][j])
                    if H[i][j] == 1:
                        dp[i][j] += Sum[i] - Sum[j - 1]
                j = j - 1
        return dp[N - 1][0] * (1 // H[N - 1][0]) - min(H[N - 1][0] - 1, 1)
