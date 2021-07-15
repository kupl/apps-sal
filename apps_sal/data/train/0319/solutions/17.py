class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        A=stoneValue
        N=len(A)
        MIN=-float('inf')
        dp=[0]*(N+1)
        
        for i in range(N-1, -1, -1):
            take=A[i]
            dp[i]=take-dp[i+1]
            if i+1<N:
                take+=A[i+1]
                dp[i]=max(dp[i], take-dp[i+2])
            if i+2<N:
                take+=A[i+2]
                dp[i]=max(dp[i], take-dp[i+3])
        if dp[0]==0:
            return 'Tie'
        return 'Alice' if dp[0]>0 else 'Bob'
