class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        N = len(A)
        dp = [[2] * N for i in range(N)]
        ans = 0
        for i in range(N):
            pos = {}
            for j in range(i):
                x = 2 * A[j] - A[i]
                if x in pos:
                    dp[i][j] = max(dp[i][j], 1 + dp[j][pos[x]])
                ans = max(ans, dp[i][j])
                pos[A[j]] = j
        return ans
        dp = [dict() for _ in range(N)]
        ret = 1
        for i in range(N):
            for j in range(i + 1, N):
                diff = A[j] - A[i]
                dp[j][diff] = dp[i].get(diff, 1) + 1
                ret = max(ret, dp[j][diff])
        return ret
