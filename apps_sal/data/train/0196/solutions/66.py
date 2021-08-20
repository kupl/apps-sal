class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        dp = [0] * n
        optsum = [A[0]] * n
        pre = A[0]
        dp[0] = A[0]
        first = dp[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + A[i], A[i])
            first = max(first, dp[i])
            pre += A[i]
            if pre > optsum[i - 1]:
                optsum[i] = pre
            else:
                optsum[i] = optsum[i - 1]
        pre = 0
        for j in range(n - 1, 0, -1):
            first = max(first, pre + A[j] + optsum[j - 1])
            pre += A[j]
        return first
