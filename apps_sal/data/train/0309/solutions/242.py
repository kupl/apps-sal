class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = defaultdict(dict)

        ans = 0

        dp[0][0] = 1

        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                ans = max(ans, dp[i][diff])

        return ans
