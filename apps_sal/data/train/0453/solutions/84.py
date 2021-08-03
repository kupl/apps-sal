class Solution:
    def minCost(self, houses: List[int], Cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dfs(i, j, k):
            if j > target:
                return float('inf')
            if i == len(houses):
                if j == target:
                    return 0
                else:
                    return float('inf')

            cost = float('inf')
            if houses[i] == 0:
                for index, c in enumerate(Cost[i]):
                    if i == 0:
                        cost = min(cost, dfs(i + 1, 1, index + 1) + c)
                    else:
                        if index + 1 == k:
                            cost = min(cost, dfs(i + 1, j, index + 1) + c)
                        else:
                            cost = min(cost, dfs(i + 1, j + 1, index + 1) + c)
                    houses[i] = 0
            else:
                if i == 0:
                    cost = dfs(i + 1, 1, houses[i])
                else:
                    if houses[i] == k:
                        cost = dfs(i + 1, j, houses[i])
                    else:
                        cost = dfs(i + 1, j + 1, houses[i])
            return cost

        ans = dfs(0, 0, 0)
        return ans if ans != float('inf') else -1
