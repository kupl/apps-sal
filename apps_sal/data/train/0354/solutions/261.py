class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        m=max(rollMax)
        dp=[[0 for i in range(m)] for j in range(6)]
        for i in range(6):
            dp[i][0]=1
        total=6
        for i in range(n-1):
            new_dp=[[0 for i in range(m)] for j in range(6)]
            new_total=0
            for j in range(6):
                new_dp[j][0]=total-sum(dp[j])
                new_dp[j][0]%=(10**9+7)
                new_total+=new_dp[j][0]
                new_total%=(10**9+7)
                for k in range(1,rollMax[j]):
                    new_dp[j][k]=dp[j][k-1]
                    new_total+=new_dp[j][k]
            dp=new_dp
            total=new_total%(10**9+7)
        return total%(10**9+7)

