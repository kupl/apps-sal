class Solution:

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        memo = {}

        def dfs(i, b, c):
            if i == m and b == target:
                return 0
            if m - i < target - b or i == m or b > target:
                return float('inf')
            key = (i, b, c)
            if key not in memo:
                if houses[i] != 0:
                    memo[key] = dfs(i + 1, b + (houses[i] != c), houses[i])
                else:
                    memo[key] = min((dfs(i + 1, b + (nc != c), nc) + cost[i][nc - 1] for nc in range(1, n + 1)))
            return memo[key]
        res = dfs(0, 0, -1)
        if res == float('inf'):
            return -1
        else:
            return res
