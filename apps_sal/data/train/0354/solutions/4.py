class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod=10**9+7
        dp=[[1]*6 for i in range(n)]
        for i in range(1,n):
            for j in range(6):
                dp[i][j]=sum([dp[i-1][k] for k in range(6)])
                if i==rollMax[j]:
                    dp[i][j]-=1
                if i>rollMax[j]:
                    dp[i][j]-=sum([dp[i-rollMax[j]-1][k] for k in range(6) if k!=j])
        return sum(dp[-1])%mod
