class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        if len(A)<=2:
            return 0
        N=len(A)
        ans=0
        dp=dict()
        dp[(A[1],A[0])]=2
        for i in range(2,N):
            for j in range(i):
                if (A[j],A[i]-A[j]) in dp:
                    z=dp[(A[j],A[i]-A[j])]
                    ans=max(z+1,ans)
                    dp[(A[i],A[j])]=z+1
                else:
                    dp[(A[i],A[j])]=2
        return ans
