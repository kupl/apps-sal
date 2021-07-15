class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        res = 2
        n = len(A)
        dp = [collections.defaultdict(int) for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                d = A[j] - A[i]
                dp[i][d] = dp[j][d] + 1
                res = max(res, dp[i][d]+1)
        return res
