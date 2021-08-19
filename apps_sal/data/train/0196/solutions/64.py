class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        currentMax = totalMax = currentMin = totalMin = A[0]
        s = A[0]
        for i in range(1, len(A)):
            currentMax = max(currentMax + A[i], A[i])
            totalMax = max(totalMax, currentMax)
            currentMin = min(currentMin + A[i], A[i])
            totalMin = min(totalMin, currentMin)
            s += A[i]
        if s - totalMin != 0:
            return max(totalMax, s - totalMin)
        else:
            return totalMax
