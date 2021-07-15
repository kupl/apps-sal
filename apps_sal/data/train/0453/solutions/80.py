from functools import lru_cache
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dp(g, i, c):
            if i == m: return 0 if g == target else sys.maxsize 
            ans = sys.maxsize 
            if houses[i] != 0:
                if houses[i] == c: ans = min(ans, dp(g, i+1, c))
                else: ans = min(ans, dp(g+1, i+1, houses[i]))
            else:
                for j in range(n):
                    if j + 1 == c: ans = min(ans, cost[i][j] + dp(g, i+1, c))
                    else: ans = min(ans, cost[i][j] + dp(g+1, i+1, j+1))
            return ans
        
        ans = dp(0, 0, 0)
        return -1 if ans >= sys.maxsize else ans

