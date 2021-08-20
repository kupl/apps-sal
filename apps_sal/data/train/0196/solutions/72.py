class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if max(A) <= 0:
            return max(A)
        endmax = [i for i in A]
        endmin = [i for i in A]
        for i in range(len(A) - 1):
            if endmax[i] > 0:
                endmax[i + 1] += endmax[i]
            if endmin[i] < 0:
                endmin[i + 1] += endmin[i]
        return max(max(endmax), sum(A) - min(endmin))
