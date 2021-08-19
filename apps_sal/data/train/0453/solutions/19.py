class Solution:

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        (dp0, dp1) = ({(0, 0): 0}, {})
        for (i, k) in enumerate(houses):
            for ik in [k] if k > 0 else range(1, n + 1):
                for (pk, pb) in dp0:
                    bb = pb + (ik != pk)
                    if bb > target:
                        continue
                    dp1[ik, bb] = min(dp1.get((ik, bb), float('inf')), dp0[pk, pb] + (0 if k > 0 else cost[i][ik - 1]))
            (dp0, dp1) = (dp1, {})
        return min([dp0[k, b] for (k, b) in dp0 if b == target] or [-1])
