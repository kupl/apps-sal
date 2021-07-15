from collections import defaultdict
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        
        dp=dict()
        mlen=0
        for i in range(len(A)):
            dp[A[i]]=defaultdict(lambda :1)
            for j in range (i-1,-1,-1):
                
                d=A[i]-A[j]
                if dp[A[i]][d]<=dp[A[j]][d]+1:
                    dp[A[i]][d]=dp[A[j]][d]+1
                    mlen=max(mlen,dp[A[i]][d])
                    
        return mlen

