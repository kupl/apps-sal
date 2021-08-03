class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = [collections.defaultdict(int) for _ in range(n)]
        res = 0
        for i in range(1, n):
            for j in range(0, i):
                diff = A[i] - A[j]
                dp[i][diff] = dp[j][diff] + 1

                res = max(res, dp[i][diff])
        return res + 1
