class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        stack = []
        
        for i, val in enumerate(A):
            if not stack or val < A[stack[-1]]:
                stack.append(i)
                
        maxWidth = 0
        
        for i in range(len(A)-1, -1, -1):
            val = A[i]
            while stack and val >= A[stack[-1]]:
                maxWidth = max(maxWidth, i - stack.pop())
            
        return maxWidth
