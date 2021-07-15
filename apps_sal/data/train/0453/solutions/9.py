class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # dp[i][c][k]: i means the ith house, c means the cth color, k means k neighbor groups
        dp = [[[math.inf for _ in range(n)] for _ in range(target + 1)] for _ in range(m)]
        
        for c in range(1, n + 1):
            if houses[0] == c: dp[0][1][c - 1] = 0
            elif not houses[0]: dp[0][1][c - 1] = cost[0][c - 1]
                
        for i in range(1, m):
            for k in range(1, min(target, i + 1) + 1):
                for c in range(1, n + 1):
                    if houses[i] and c != houses[i]: continue
                    same_neighbor_cost = dp[i - 1][k][c - 1]
                    diff_neighbor_cost = min([dp[i - 1][k - 1][c_] for c_ in range(n) if c_ != c - 1] or [math.inf])
                    paint_cost = cost[i][c - 1] * (not houses[i])
                    dp[i][k][c - 1] = min(same_neighbor_cost, diff_neighbor_cost) + paint_cost
        res = min(dp[-1][-1])
        return res if res < math.inf else -1
            
        
        
        

