class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        dp = collections.defaultdict(dict)
        ans = 0

        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] = dp[i].get(diff, 0)
                dp[i][diff] = max(dp[i][diff], dp[j].get(diff, 0) + 1)
                ans = max(ans, dp[i][diff])
        return ans + 1
