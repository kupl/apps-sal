class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        t = target
        dp = [[[0 for i in range(t+1)] for j in range(n+1)] for i in range(m+1)]
        for k in range(1,t+1):
            for j in range(1,n+1):
                dp[0][j][k] = 10**9
        for i in range(1,m+1):    
            for j in range(1,n+1):
                dp[i][j][0] = 10**9
        for i in range(1,m+1):
            for j in range(1,n+1):
                for k in range(1,t+1):
                    if houses[i-1] == j and k<=i:
                        dp[i][j][k] = min(dp[i-1][j][k],min([dp[i-1][p][k-1] if p!=j else 10**9 for p in range(1,n+1)]))
                    elif houses[i-1]==0 and k<=i:
                        dp[i][j][k] = cost[i-1][j-1]+min(dp[i-1][j][k],min([dp[i-1][p][k-1] if p!=j else 10**9 for p in range(1,n+1)]))
                    else:
                        dp[i][j][k] = 10**9
                        
        ans = 10**9
        for j in range(1,n+1):
            ans = min(ans, dp[m][j][t])
        return ans if ans<10**9 else -1
