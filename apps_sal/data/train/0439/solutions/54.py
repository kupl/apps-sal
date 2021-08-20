class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        dp = [[1, 1] for i in range(len(A))]
        res = 1
        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                continue
            if A[i] > A[i - 1]:
                dp[i][0] = max(dp[i][0], dp[i - 1][1] + 1)
            else:
                dp[i][1] = max(dp[i][1], dp[i - 1][0] + 1)
            res = max(res, dp[i][0], dp[i][1])
        return res
