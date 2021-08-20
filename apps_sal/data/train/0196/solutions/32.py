class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        (curmax, curmin) = (0, 0)
        total = 0
        maxsum = minsum = A[0]
        for num in A:
            curmax = max(num, curmax + num)
            maxsum = max(maxsum, curmax)
            curmin = min(num, curmin + num)
            minsum = min(minsum, curmin)
            total += num
        return max(maxsum, total - minsum) if maxsum > 0 else maxsum
