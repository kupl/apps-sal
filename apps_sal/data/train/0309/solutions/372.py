class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        m = 1001
        dp = [[1] * (m + 1) for _ in range(n)]
        ans = float('-inf')
        for i in range(1, n):
            for k in range(i):
                dp[i][A[i] - A[k] + 500] = max(dp[i][A[i] - A[k] + 500], 1 + dp[k][A[i] - A[k] + 500])
            ans = max(max(dp[i]), ans)
        return ans
