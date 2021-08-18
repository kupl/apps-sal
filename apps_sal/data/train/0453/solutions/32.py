class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, t: int) -> int:
        mem = {}

        def recurse(i, lastc, target):
            if target < 0:
                return float('inf')
            if i == m:
                return float('inf') if target != 0 else 0
            if (i, lastc, target) not in mem:
                if houses[i] > 0:
                    mem[(i, lastc, target)] = recurse(i + 1, houses[i], target - 1 if lastc != houses[i] else target)
                else:
                    if lastc > 0:
                        mem[(i, lastc, target)] = recurse(i + 1, lastc, target) + cost[i][lastc - 1]
                    else:
                        mem[(i, lastc, target)] = float('inf')
                    for j in range(1, n + 1):
                        if j != lastc:
                            mem[(i, lastc, target)] = min(recurse(i + 1, j, target - 1) + cost[i][j - 1], mem[(i, lastc, target)])
            return mem[(i, lastc, target)]

        result = recurse(0, 0, t)
        if result == float('inf'):
            return -1
        return result
