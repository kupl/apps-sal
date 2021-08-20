class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        result = currLen = 0
        for i in range(len(A)):
            if i >= 2 and (A[i - 2] > A[i - 1] < A[i] or A[i - 2] < A[i - 1] > A[i]):
                currLen += 1
            elif i >= 1 and A[i - 1] != A[i]:
                currLen = 2
            else:
                currLen = 1
            result = max(result, currLen)
        return result
