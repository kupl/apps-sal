class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max1 = -float('inf')
        maxc = -float('inf')
        for i in range(len(A)):
            maxc = max(maxc + A[i], A[i])
            max1 = max(max1, maxc)

        min1 = float('inf')
        minc = float('inf')
        for i in range(len(A)):
            minc = min(minc + A[i], A[i])
            min1 = min(min1, minc)

        if min1 == sum(A):
            return max1

        return max(max1, sum(A) - min1)
