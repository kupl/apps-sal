class Solution:

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        m = len(houses)
        n += 1

        @lru_cache(None)
        def minCost(i, n_nei, prev_c):
            if i == m:
                if n_nei == target:
                    return 0
                return float('inf')
            if n_nei > target:
                return float('inf')
            if houses[i] != 0:
                if houses[i] == prev_c:
                    return minCost(i + 1, n_nei, prev_c)
                return minCost(i + 1, n_nei + 1, houses[i])
            return min((minCost(i + 1, n_nei if c == prev_c else n_nei + 1, c) + cost[i][c - 1] for c in range(1, n)))
        res = minCost(0, 0, -1)
        return res if res != float('inf') else -1
