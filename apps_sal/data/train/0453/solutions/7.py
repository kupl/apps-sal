class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        maxc = 10**9
        N = len(houses)
        dp = [[[None]*(target+1) for _ in range(n+1)] for _ in range(m)]
        
        def solve(i,j,k):
            if k < 0: return maxc
            if dp[i][j][k] is None:
                if i == N - 1:
                    if k != 0:
                        dp[i][j][k] = maxc
                    else:
                        if houses[i] == 0:
                            dp[i][j][k] = cost[i][j-1]
                        else:
                            dp[i][j][k] = 0
                else:
                    dp[i][j][k] = cost[i][j-1] if houses[i] == 0 else 0
                    if houses[i+1] == 0:
                        dp[i][j][k] += min([solve(i+1, jj, k-1 if jj != j else k) for jj in range(1, n+1)])
                    elif houses[i+1] == j:
                        dp[i][j][k] += solve(i+1, j, k)
                    else:
                        dp[i][j][k] += solve(i+1, houses[i+1], k-1)
            return dp[i][j][k]
        
        if houses[0] == 0:
            result = min([solve(0, j, target-1) for j in range(1, n+1)])
        else:
            result = solve(0, houses[0], target-1)
        
        return result if result < maxc else -1

