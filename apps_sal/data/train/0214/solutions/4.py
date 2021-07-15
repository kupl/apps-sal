class Solution:
    def movesToMakeZigzag(self, A: List[int]) -> int:
        res1=0
        n=len(A)
        B=A.copy()
        for i in range(1,n,2):
            if A[i-1]<=A[i]:
                t=A[i]-A[i-1]+1
                res1+=t
                A[i]=A[i-1]-1
            if i+1<n and A[i+1]<=A[i]:
                t=A[i]-A[i+1]+1
                res1+=t
                A[i]=A[i+1]-1
        res2=0
        for i in range(0,n,2):
            if i-1>=0 and B[i]>=B[i-1]:
                t=B[i]-B[i-1]+1
                res2+=t
                B[i]=B[i-1]-1
            if i+1<n and B[i+1]<=B[i]:
                t=B[i]-B[i+1]+1
                res2+=t
                B[i]=B[i+1]-1
        # print(A)
        # print(B)
        # print(res1,res2)
        return min(res1,res2)
