class Solution:

    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        dp = [[[-1] * (2 * n) for _ in range(n)] for _ in range(n)]
        return self.search(graph, dp, 1, 2, 0)

    def search(self, graph, dp, x, y, z):
        if z == 2 * len(graph):
            return 0
        if dp[x][y][z] == -1:
            if x == 0:
                res = 1
            elif x == y:
                res = 2
            elif z % 2 == 0:
                (draw, res) = (False, None)
                for nx in graph[x]:
                    ans = self.search(graph, dp, nx, y, z + 1)
                    if ans == 1:
                        res = 1
                        break
                    elif ans == 0:
                        draw = True
                res = res if res else 0 if draw else 2
            else:
                (draw, res) = (False, None)
                for ny in graph[y]:
                    if ny == 0:
                        continue
                    ans = self.search(graph, dp, x, ny, z + 1)
                    if ans == 2:
                        res = 2
                        break
                    elif ans == 0:
                        draw = True
                res = res if res else 0 if draw else 1
            dp[x][y][z] = res
        return dp[x][y][z]
