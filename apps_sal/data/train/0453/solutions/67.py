import functools


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        @functools.lru_cache(None)
        def dfs(i, last_color, hoods):
            if hoods > target:
                return float('inf')

            if i >= m:
                if hoods != target:
                    return float('inf')
                return 0

            if houses[i] != 0:
                if houses[i] - 1 == last_color:
                    return dfs(i + 1, houses[i] - 1, hoods)
                else:
                    return dfs(i + 1, houses[i] - 1, hoods + 1)
            else:
                cands = []
                for color in range(n):
                    if color == last_color:
                        cands.append(cost[i][color] + dfs(i + 1, color, hoods))
                    else:
                        cands.append(cost[i][color] + dfs(i + 1, color, hoods + 1))
                return min(cands)

        ans = dfs(0, -1, 0)

        if ans == float('inf'):
            return -1
        return ans
