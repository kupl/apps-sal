class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        memo = [[[-1 for i in range(m+1)] for j in range(n+1)] for _ in range(m+1)]
        def dp(i, prevColor, nbrs):
            if nbrs > target : return float('inf')
            if i == m:
                if nbrs == target: return 0
                else: return float('inf')
            
            if memo[i][prevColor][nbrs] != -1: return memo[i][prevColor][nbrs]
            ans = float('inf')
            if houses[i] == 0:
                for j in range(n):
                    if j+1 == prevColor:
                        temp = dp(i+1, j+1, nbrs)
                    else:
                        temp = dp(i+1, j+1, nbrs+1)
                    ans = min(ans, cost[i][j]+ temp)
            else:
                if prevColor == houses[i]:
                    ans = min(ans, dp(i+1, houses[i], nbrs))
                else:
                    ans = min(ans, dp(i+1, houses[i], nbrs+1))
            memo[i][prevColor][nbrs] = ans
            return ans
        ans = dp(0,0,0)
        if ans == float('inf'): return -1
        else: return ans

