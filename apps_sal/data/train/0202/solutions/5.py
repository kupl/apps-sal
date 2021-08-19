class Solution:

    def longestMountain(self, A: List[int]) -> int:
        leftIncreasing = [0 for x in range(len(A))]
        rightIncreasing = [0 for x in range(len(A))]
        for x in range(1, len(A)):
            if A[x] > A[x - 1]:
                leftIncreasing[x] += leftIncreasing[x - 1] + 1
            if A[len(A) - 1 - x] > A[len(A) - x]:
                rightIncreasing[len(A) - 1 - x] += rightIncreasing[len(A) - x] + 1
        result = 0
        for x in range(len(A)):
            if leftIncreasing[x] and rightIncreasing[x]:
                result = max(result, leftIncreasing[x] + rightIncreasing[x] + 1)
        return result if result >= 3 else 0
