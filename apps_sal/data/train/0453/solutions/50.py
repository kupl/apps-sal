import numpy as np
from collections import defaultdict


class Solution:

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        INF = int(1000000000.0)
        DP = defaultdict(lambda: INF)
        if houses[0] == 0:
            for col in range(1, n + 1):
                DP[1, col] = cost[0][col - 1]
        else:
            DP[1, houses[0]] = 0
        for i in range(1, m):
            NDP = defaultdict(lambda: INF)
            ByGroups = defaultdict(list)
            for (key, min_cost) in DP.items():
                (groups_prev, col_prev) = key
                ByGroups[groups_prev].append((min_cost, col_prev))
            curr_colors = range(1, n + 1) if houses[i] == 0 else [houses[i]]
            for (groups_prev, prev_colors_array) in ByGroups.items():
                prev_colors_array.sort()
                prev_colors = [col_prev for (min_cost, col_prev) in prev_colors_array[:2]]
                for col_curr in curr_colors:
                    paint_cost = cost[i][col_curr - 1] if houses[i] == 0 else 0
                    for col_prev in [col_curr] + prev_colors:
                        groups_curr = groups_prev + (col_prev != col_curr)
                        curr_cost = DP[groups_prev, col_prev] + paint_cost
                        if groups_curr <= target and curr_cost < INF:
                            key = (groups_curr, col_curr)
                            NDP[key] = min(NDP[key], curr_cost)
            DP = NDP
        ans = -1
        for (key, min_cost) in DP.items():
            if key[0] == target and (ans < 0 or ans > min_cost):
                ans = min_cost
        return ans
