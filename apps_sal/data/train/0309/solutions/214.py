class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        ans = 0
        n = len(A)
        dp = [collections.defaultdict(int) for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                diff = A[i] - A[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                ans = max(ans, dp[i][diff])
        return ans
