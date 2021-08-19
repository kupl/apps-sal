class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        i = 0
        j = 0
        numZeros = 0
        bestSize = 0
        while j < len(A):
            if A[j] == 1:
                pass
            elif A[j] == 0:
                numZeros += 1
                while numZeros > K:
                    if i >= 0 and A[i] == 0:
                        numZeros -= 1
                    i += 1
            bestSize = max(bestSize, j - i + 1)
            j += 1
        return bestSize
