class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        if not houses:
            return 0
        size = len(houses)
        memo = dict()

        def dfs(index, t, p):
            key = (index, t, p)
            if key in memo:
                return memo[key]
            if index == size or t > size - index or t < 0:
                if index == size and t == 0:
                    return 0
                else:
                    return float('inf')
            temp = float('inf')
            if houses[index] == 0:
                for nc in range(1, n + 1):
                    temp = min(temp, dfs(index + 1, t - (nc != p), nc) + cost[index][nc - 1])
            else:
                temp = dfs(index + 1, t - (p != houses[index]), houses[index])
            memo[key] = temp
            return temp

        res = dfs(0, target, -1)
        return res if res < float('inf') else -1
