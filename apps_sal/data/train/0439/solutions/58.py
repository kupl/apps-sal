class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)
        if n == 1:
            return 1
        dp = [[1, 1] for i in range(n)]
        ans = 1
        for i in range(1, n):
            if A[i] > A[i - 1]:
                dp[i][0] += dp[i - 1][1]
            if A[i] < A[i - 1]:
                dp[i][1] += dp[i - 1][0]
            ans = max(ans, dp[i][0], dp[i][1])
        return ans
