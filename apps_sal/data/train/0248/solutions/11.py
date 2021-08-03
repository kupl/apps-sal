class UnionFind:
    def __init__(self, row_size, col_size):
        self.roots = [[(i, j) for j in range(col_size)]
                      for i in range(row_size)]

    def get_rank(self, node):
        return -node[0] * len(self.roots[0]) - node[1]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            if self.get_rank(root1) > self.get_rank(root2):
                self.roots[root2[0]][root2[1]] = root1
            else:
                self.roots[root1[0]][root1[1]] = root2

    def find(self, node):
        if self.roots[node[0]][node[1]] != node:
            self.roots[node[0]][node[1]] = self.find(self.roots[node[0]][node[1]])
        return self.roots[node[0]][node[1]]


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        row_size, col_size = len(grid), len(grid[0])
        uf = UnionFind(row_size, col_size)
        for i in range(row_size):
            for j in range(col_size):
                for (x, y) in [(i - 1, j), (i, j - 1)]:
                    if x >= 0 and y >= 0 and grid[x][y] == grid[i][j]:
                        if uf.find((i, j)) == uf.find((x, y)):
                            return True
                        uf.union((i, j), (x, y))
        return False
