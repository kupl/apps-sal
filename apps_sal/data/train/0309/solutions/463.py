class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        N = len(A)
        dp = [collections.defaultdict(int) for _ in range(N)]
        res = 0
        for i in range(1, N):
            for j in range(i):
                delta = A[i] - A[j]
                dp[i][delta] = max(dp[i][delta], dp[j][delta] + 1, 2)
                res = max(res, dp[i][delta])
        return res
