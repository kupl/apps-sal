class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        dp1, dp2 = [0] * n, [0] * n

        for i in range(n - L + 1):
            if i == 0:
                dp1[i] = sum(A[i:i + L])
            else:
                dp1[i] = dp1[i - 1] + A[i + L - 1] - A[i - 1]

        maxy = 0
        for i in range(n - M + 1):
            if i == 0:
                dp2[i] = sum(A[i:i + M])
            else:
                dp2[i] = dp2[i - 1] + A[i + M - 1] - A[i - 1]

            if i >= L:
                maxy = max(maxy, dp2[i] + max(dp1[:i - L + 1]))
            if i + M < n:
                maxy = max(maxy, dp2[i] + max(dp1[i + M:]))

        return maxy
