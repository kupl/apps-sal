class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        def dp(i, color, target):
            if target < 0: return float('inf')
            if cache[i][color][target] < 0:
                if houses[i] > 0 and color != houses[i] - 1:
                    cache[i][color][target] = float('inf')
                elif i == m - 1:
                    if target > 0:
                        cache[i][color][target] = float('inf')
                    else:
                        cache[i][color][target] = cost[i][color] if houses[i] == 0 else 0
                else:
                    cost1 = cost[i][color] if houses[i] == 0 else 0
                    cost2 = min(dp(i+1, c, target - int(c != color)) for c in range(n))
                    cache[i][color][target] = cost1 + cost2
            return cache[i][color][target]
        
        cache = [[[-1] * target for _ in range(n)] for _ in range(m)]
        res = min(dp(0, c, target-1) for c in range(n))
        return -1 if res == float('inf') else res
