class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        
        stack,n = [],len(A)
        maxy = 0
        i = 0
        for i,v in enumerate(A):
            if stack and maxy+stack[0][1]>=n: break
            if not stack or v<stack[-1][0]:
                stack.append((v,i))
                continue
            
            j = -1
            while j>=-1*len(stack) and v>=stack[j][0]:
                maxy = max(maxy, i-stack[j][1])
                j-=1
            
                
        return maxy
