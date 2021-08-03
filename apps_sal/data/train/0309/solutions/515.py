class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        res = 0
        dp = [collections.defaultdict(lambda: 1) for _ in range(len(A))]
        for i in range(len(A)):
            for k in range(i - 1, -1, -1):
                dp[i][A[i] - A[k]] = max(dp[i][A[i] - A[k]], dp[k][A[i] - A[k]] + 1)  # remember the MAX here!!!
                res = max(res, dp[i][A[i] - A[k]])
        return res
