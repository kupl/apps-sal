class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        A = arr
        N = len(A)
        dp0 = [None] * N
        dp1 = [None] * N

        cur = A[0]
        dp0[0] = cur
        for i in range(1, N):
            cur = max(cur + A[i], A[i])
            dp0[i] = cur

        cur = A[-1]
        dp1[-1] = cur
        for i in range(N - 2, -1, -1):
            cur = max(cur + A[i], A[i])
            dp1[i] = cur

        ans = max(dp0)
        for i, x in enumerate(A):
            if i + 2 < N:
                ans = max(ans, dp0[i] + dp1[i + 2])
        return ans
