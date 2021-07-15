class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = [collections.defaultdict(lambda: 1) for _ in range(n)]
        ans = 0
        for i in range(1, n):
            for j in range(0, i):
                diff = A[i] - A[j]
                dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)
                ans = max(ans, dp[i][diff])
        return ans
                

