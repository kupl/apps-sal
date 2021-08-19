class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        totalSize = 1
        i = 0
        while i < len(A) - totalSize:
            currentSize = 1
            sign = None
            for j in range(i + 1, len(A)):
                currentSign = None
                if A[j] > A[j - 1]:
                    currentSign = 1
                elif A[j] < A[j - 1]:
                    currentSign = -1
                else:
                    break
                if currentSign != sign:
                    currentSize += 1
                    sign = currentSign
                else:
                    break
            totalSize = max(totalSize, currentSize)
            i += 1
        return totalSize
