class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        dp = [[0, 0] for _ in range(n)]

        for i in range(L - 1, n):  # scan from left to right, get all dp[i][0] first
            if i > 0:
                dp[i][0] = max(dp[i - 1][0], sum(A[i - L + 1:i + 1:+1]))
            else:
                dp[i][0] = A[0]

        for i in range(n - L, -1, -1):  # scan from left to right, get all dp[i][0] first
            if i < n - 1:
                dp[i][1] = max(dp[i + 1][1], sum(A[i:i + L:+1]))

            else:
                dp[i][1] = A[n - 1]
        # print(dp)
        maximum = float('-inf')
        # Then for subarray M
        for i in range(0, n - M + 1):
            s = sum(A[i:i + M:1])
            left = dp[i - 1][0] if i - 1 > 0 else 0
            right = dp[i + M][1] if i + M < n else 0
            #print(i,s, left, right)
            maximum = max(maximum, s + left, s + right)
        return maximum
