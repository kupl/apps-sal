class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        #stack maintains the index of strictly descending numbers
        stack = []
        for i,v in enumerate(A):
            if i==0 or v<A[stack[-1]]:
                stack.append(i)
        ans = 0
        for i in range(len(A)-1,-1,-1):
            #if A[i]<A[stack[-1]], then it must be smaller than all
            #the prev elements in stack, 
            #since stack is increasing (by popping)
            
            #then wait until larger elements
            #maybe we can find longer ramp
            while stack and A[i]>=A[stack[-1]]:
                ans = max(ans,i-stack.pop())
        return ans
