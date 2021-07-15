class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        n = len(A)
        rightMax = [0 for i in range(n+1)]
        
        for i in range(n-1, -1, -1):
            rightMax[i] = max(rightMax[i+1], A[i])
        
        i = 0
        j = 0
        result = 0
        
        while i < n and j < n:
            if A[i] <= rightMax[j]:
                result = max(result, j - i)
                j += 1
            else:
                i += 1
        return result
