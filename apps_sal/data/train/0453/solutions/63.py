class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # dp[i][j][k] is the minimum cost to paint {0, 1, ..., `i`} houses of `j` neighborhoods, and the `i`th house is painted as color `k`
        
        dp = [[[math.inf for k in range(n)] for j in range(target)] for i in range(m)]
        
        pre = None
        min_neighborhoods = 1
        for i in range(m):
            if houses[i]:
                if pre is not None and houses[i] != pre:
                    min_neighborhoods += 1
                pre = houses[i]
            if i == 0:
                if houses[i]:
                    k = houses[i]-1
                    dp[i][0][k] = 0
                else:
                    for k in range(n):
                        dp[i][0][k] = cost[i][k]
                continue
            for j in range(min_neighborhoods-1, min(i+1, target)):
                if houses[i]:
                    k = houses[i]-1
                    dp[i][j][k] = min(min(dp[i-1][j-1][p] for p in range(n) if p != k), dp[i-1][j][k])
                else:
                    for k in range(n):
                        dp[i][j][k] = cost[i][k] + min(min(dp[i-1][j-1][p] for p in range(n) if p != k), dp[i-1][j][k])

        ans = min(dp[-1][-1])
        if ans == math.inf:
            return -1
        else:
            return ans
