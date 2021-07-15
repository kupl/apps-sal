class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        m_ = {}
        
        def dp(i, t, color):
            key =  (i, t, color)
            if key in m_: return m_[key]
            if t == 0 and i == len(houses): return 0
            if t < 0 or t > m - i: return float('inf')
            if houses[i] == 0:
                m_[key] = min(dp(i + 1, t - (c != color), c) + cost[i][c - 1] for c in range(1, n + 1))
            else:
                m_[key] = dp(i + 1, t - (houses[i] != color), houses[i])
            
            return m_[key]
        
        ans = dp(0, target, -1)
        
        return ans if ans < float('inf') else -1
