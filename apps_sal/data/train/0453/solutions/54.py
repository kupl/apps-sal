class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        memo = {}

        def dfs(i, k, target):
            if target < 0 or target > m - i:
                return float('inf')
            if i == m:
                return 0 if target == 0 else float('inf')
            if (i, k, target) not in memo:
                if houses[i]:
                    memo[i, k, target] = dfs(i + 1, houses[i], target - (houses[i] != k))
                else:
                    memo[i, k, target] = min(cost[i][a - 1] + dfs(i + 1, a, target - (a != k)) for a in range(1, n + 1))
            return memo[i, k, target]
        ans = dfs(0, 0, target)
        return ans if ans < float('inf') else -1
