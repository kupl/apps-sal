
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if A==[]: return 0
        if len(A)==1: return 1
        dp={}
        for i in range(0,len(A)):
            for j in range(0,i):
                dp[i,A[i]-A[j]]=dp.get((j,A[i]-A[j]),0)+1
        
        return max(dp.values())+1

