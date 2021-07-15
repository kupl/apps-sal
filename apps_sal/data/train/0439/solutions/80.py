class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        maxLength = 0
        length = 0
        
        for i in range(len(A)):
            if i >= 2 and ( A[i - 2] > A[i - 1] < A[i] or A[i - 2] < A[i - 1] > A[i]):
                length += 1
            elif i >= 1 and A[i - 1] != A[i]:
                length = 2
            else:
                length = 1
            maxLength = max(maxLength, length)
        
        return maxLength
