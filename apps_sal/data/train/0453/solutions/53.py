class Solution:

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        memo = {}

        def dfs(i, j, target):
            if target < 0 or target > m - i:
                return float('inf')
            if i == m:
                if target == 0:
                    return 0
                else:
                    return float('inf')
            if (i, j, target) not in memo:
                if houses[i]:
                    memo[i, j, target] = dfs(i + 1, houses[i], target - (houses[i] != j))
                else:
                    memo[i, j, target] = min((cost[i][k - 1] + dfs(i + 1, k, target - (k != j)) for k in range(1, n + 1)))
            return memo[i, j, target]
        ans = dfs(0, 0, target)
        return ans if ans < float('inf') else -1
