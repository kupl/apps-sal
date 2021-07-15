class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        stack = []
        #prev = float('inf')
        for i,v in enumerate(A):
            if i==0 or v<A[stack[-1]]:
                stack.append(i)
        
        ans = 0
        #print(stack)
        for j in range(len(A)-1,-1,-1):
            i = j
            while stack and A[j]>=A[stack[-1]]:
                i = stack.pop()
            
            ans = max(ans,j-i)
        return ans    
