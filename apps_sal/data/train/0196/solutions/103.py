class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # there are two cases, one, includes end points, two, not include end points
        ans = float('-inf')
        csum = 0
        for x in A:
            csum = max(x, csum + x)
            ans = max(ans, csum)

        mi = float('inf')
        csum = 0  # notice that it can be zero
        for i in range(1, len(A) - 1):
            csum = min(csum + A[i], A[i])
            mi = min(mi, csum)

        ans = max(ans, sum(A) - mi)
        return ans
