class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        res = 0
        dp = {i:collections.defaultdict(lambda: 1) for i in range(len(A))}
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i]-A[j]
                dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)
                res = max(res, dp[i][diff])
        return res
