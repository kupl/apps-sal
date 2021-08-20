class Solution:

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        f = [[-1] * n for i in range(target + 1)]
        if houses[0]:
            f[1][houses[0] - 1] = 0
        else:
            for k in range(n):
                f[1][k] = cost[0][k]
        for i in range(1, m):
            g = [[-1] * n for i in range(target + 1)]
            for j in range(1, min(i + 1, target) + 1):
                for k in range(n):
                    if houses[i] and houses[i] - 1 != k:
                        continue
                    g[j][k] = f[j][k]
                    for l in range(n):
                        if l != k and f[j - 1][l] != -1:
                            if g[j][k] == -1 or f[j - 1][l] < g[j][k]:
                                g[j][k] = f[j - 1][l]
                    if g[j][k] != -1 and (not houses[i]):
                        g[j][k] += cost[i][k]
            f = g
        ans = list(filter(lambda x: x != -1, f[target]))
        if not ans:
            return -1
        else:
            return min(ans)
