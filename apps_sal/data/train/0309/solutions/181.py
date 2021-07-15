class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        #9,4,7,2,10
        #0,5,2,7,-1
        N=len(A)
        dp={}
        for i in range(N):
            for j in range(i+1,N):
                dp[j,A[j]-A[i]]=dp.get((i,A[j]-A[i]),1)+1
        return max(dp.values())

