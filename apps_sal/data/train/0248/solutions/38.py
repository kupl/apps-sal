class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]

    def find(self, i):
        if self.parents[i] == i:
            return i
        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def unite(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        self.parents[pb] = pa
        return

    def same(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        return pa == pb


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        dx = [1, 0]
        dy = [0, 1]
        N = len(grid)
        M = len(grid[0])
        ALL = N * M
        # print(\"size\", N, M, ALL)
        tree = UnionFind(ALL)
        for i in range(N):
            for j in range(M):
                for k in range(2):
                    if 0 <= i + dx[k] < N and 0 <= j + dy[k] < M:
                        if grid[i][j] == grid[i + dx[k]][j + dy[k]]:
                            # print(i, j, k)
                            # print((i+dx[k])*M+j+dy[k])
                            if tree.same(i * M + j, (i + dx[k]) * M + j + dy[k]):
                                return True
                            tree.unite(i * M + j, (i + dx[k]) * M + j + dy[k])
        return False
