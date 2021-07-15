class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if not A or len(A)==1: return 0
        m=len(A)
        up,down=[0 for i in range(m)],[0 for i in range(m)]
        up[0], down[-1]=0,0
        for i in range(1,m):
            j=m-1-i
            if A[i]>A[i-1]:
                up[i]=up[i-1]+1
            else:up[i]=0
            if A[j]>A[j+1]:
                down[j]=down[j+1]+1
            else: down[j]=0
        ans=0
        for i in range(m):
            if up[i] and down[i]: ## need peak
                ans=max(ans,up[i]+down[i]+1)
        return ans
            
        
            
                

