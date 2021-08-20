class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        ans = cur = float('-inf')
        for v in A:
            cur = v + max(cur, 0)
            ans = max(ans, cur)
        rightsum = [0] * n
        rightsum[-1] = A[-1]
        for i in range(n - 2, -1, -1):
            rightsum[i] = rightsum[i + 1] + A[i]
        rightmax = [0] * n
        rightmax[-1] = rightsum[-1]
        for i in range(n - 2, -1, -1):
            rightmax[i] = max(rightmax[i + 1], rightsum[i])
        cur = 0
        for i in range(n - 2):
            cur += A[i]
            ans = max(ans, cur + rightmax[i + 2])
        return ans
