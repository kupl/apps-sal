class Solution:
    def onTrack(self, neighbours, visited, m, target):
        return neighbours <= target and neighbours + m - visited >= target

    def minCost(self, houses, cost, m: int, n: int, target: int) -> int:
        dp = {}
        if not self.onTrack(1, 1, m, target):
            return -1
        if houses[0] != 0:
            dp[houses[0]] = {1: 0}
        else:
            for color in range(1, n + 1):
                dp[color] = {1: cost[0][color - 1]}
        # Start iteration
        for each in range(1, m):
            new = {}
            if houses[each] != 0:
                colors = list(range(houses[each], houses[each] + 1))
            else:
                colors = list(range(1, n + 1))
            for new_color in colors:
                for color in list(dp.keys()):
                    isNew = int(color != new_color)
                    for neighbours in list(dp[color].keys()):
                        if self.onTrack(neighbours + isNew, each + 1, m, target):
                            if new_color not in list(new.keys()):
                                new[new_color] = {}
                            new_cost = dp[color][neighbours] + cost[each][new_color - 1] * int(houses[each] == 0)
                            last = new_cost
                            if neighbours + isNew in list(new[new_color].keys()):
                                last = min(new_cost, new[new_color][neighbours + isNew])
                            new[new_color][neighbours + isNew] = last
            if not new:
                return -1
            dp = new
        result = float('inf')
        for color in list(dp.keys()):
            if target in list(dp[color].keys()):
                result = min(result, dp[color][target])
        if result != float('inf'):
            return result
        else:
            return -1
