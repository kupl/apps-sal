class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        stack=[]
        res=0
        for i,a in enumerate(A):
            if not stack or stack[-1][1]>a:
                stack.append([i,a])
            else:
                j=len(stack)-1
                while j>=0 and stack[j][1]<=a:
                    res=max(res,i-stack[j][0])
                    j-=1
        return res
