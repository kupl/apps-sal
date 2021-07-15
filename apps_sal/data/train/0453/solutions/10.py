class Solution:
    def minCost(self, houses: List[int], costs: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def helper(hIdx, prevColor, groups):
            if hIdx == m:
                return 0 if groups == target else float('inf')
            if houses[hIdx]: # painted
                return helper(hIdx + 1, houses[hIdx], groups + int(houses[hIdx] != prevColor))
            total = float('inf')
            for c in range(1, n+1):
                total = min(total, costs[hIdx][c-1] + helper(hIdx+1, c, groups + int(c != prevColor)))
            return total
        
        res = helper(0, 0, 0)
        return res if res < 10 ** 9 else -1

