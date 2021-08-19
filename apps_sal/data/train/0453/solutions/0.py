class Solution:

    def minCost(self, houses: List[int], Cost: List[List[int]], m: int, n: int, target: int) -> int:

        @lru_cache(None)
        def dfs(i, j, k):
            if i == len(houses):
                if j == target:
                    return 0
                else:
                    return float('inf')
            if houses[i] != 0:
                return dfs(i + 1, int(houses[i] != k) + j, houses[i])
            cost = float('inf')
            for (index, c) in enumerate(Cost[i]):
                cost = min(cost, dfs(i + 1, int(index + 1 != k) + j, index + 1) + c)
            return cost
        return dfs(0, 0, 0) if dfs(0, 0, 0) != float('inf') else -1
