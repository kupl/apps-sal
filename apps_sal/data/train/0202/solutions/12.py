class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n=len(A)
        left_inc=[0]*n
        for i in range(1,n):
            if A[i]>A[i-1]:
                left_inc[i]=1+left_inc[i-1]
        print(left_inc)
        
        right_inc=[0]*n
        for i in range(n-2,-1,-1):
            if A[i]>A[i+1]:
                right_inc[i]=1+right_inc[i+1]
        print(right_inc)
        
        res=0
        for i in range(n):
            if left_inc[i]!=0 and right_inc[i]!=0:
                res=max(res,left_inc[i]+right_inc[i]+1)
        
        return res if res>=3 else 0
