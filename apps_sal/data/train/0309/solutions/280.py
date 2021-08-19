class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        m = max(A) - min(A) + 1
        n = len(A)
        dp = [[1 for _ in range(2 * m)] for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                d = A[j] - A[i]
                if d < 0:
                    d = m + abs(d)
                dp[j][d] = dp[i][d] + 1
                ans = max(ans, dp[j][d])
        return ans
