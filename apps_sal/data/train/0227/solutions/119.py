class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        i = 0
        j = 0
        maxValue = 0
        numZeros = 0
        while j < len(A):
            if not A[j]:
                if numZeros < K:
                    numZeros += 1
                    j += 1
                else:
                    maxValue = max(maxValue, j - i)
                    while i <= j and A[i]:
                        i += 1
                    i += 1
                    j += 1
            else:
                j += 1
        maxValue = max(maxValue, j - i)
        return maxValue
