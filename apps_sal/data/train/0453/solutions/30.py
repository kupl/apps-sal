class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        memo = {}
        def dfs(idx, groups, prev_color):
            nonlocal target, m, n
            if (idx, groups, prev_color) in memo:
                return memo[(idx, groups, prev_color)]
            if groups > target:
                return sys.maxsize 
            if idx == len(houses):
                if groups == target:
                    return 0
                return sys.maxsize 
            else:
                if houses[idx] != 0:
                    return dfs(idx + 1, groups + (1 if houses[idx] != prev_color else 0), houses[idx])
                else:
                    low = sys.maxsize
                    for i in range(n):
                        low = min(low,cost[idx][i] + dfs(idx + 1, groups + (1 if (i + 1) != prev_color else 0), i + 1))
                    memo[(idx, groups, prev_color)] = low
                    return memo[(idx, groups, prev_color)]
        ans = dfs(0, 0, -1)
        return -1 if ans == sys.maxsize else ans
