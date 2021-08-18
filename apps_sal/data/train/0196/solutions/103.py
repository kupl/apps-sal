class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        ans = float('-inf')
        csum = 0
        for x in A:
            csum = max(x, csum + x)
            ans = max(ans, csum)

        mi = float('inf')
        csum = 0
        for i in range(1, len(A) - 1):
            csum = min(csum + A[i], A[i])
            mi = min(mi, csum)

        ans = max(ans, sum(A) - mi)
        return ans
