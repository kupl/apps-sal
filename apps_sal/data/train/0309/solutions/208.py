class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        N = len(A)
        dp = [dict() for _ in range(N)]
        ret = 1
        for i in range(N):
            for j in range(i + 1, N):
                diff = A[j] - A[i]
                dp[j][diff] = dp[i].get(diff, 1) + 1
                ret = max(ret, dp[j][diff])
        return ret
