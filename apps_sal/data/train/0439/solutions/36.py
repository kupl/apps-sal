class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A)==1:
            return 1

        dp=[0]*len(A)
        dp[0]=1
        dp[1]=2 if A[1]!=A[0] else 1
        
        if A[1]>A[0]:
            last=1
        elif A[1]<A[0]:
            last=-1
        else:
            last=0
           
        ans=max(dp[0],dp[1])
        
        for i in range(2,len(A)):
            if (A[i]>A[i-1] and last==-1) or (A[i]<A[i-1] and last==1):
                dp[i]=dp[i-1]+1
            elif A[i]==A[i-1]:
                dp[i]=1
            else:
                dp[i]=2
    
            ans=max(ans,dp[i])
            if A[i]>A[i-1]:
                last=1
            elif A[i]<A[i-1]:
                last=-1
            else:
                last=0
            
        return ans

