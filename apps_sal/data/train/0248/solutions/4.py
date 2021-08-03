class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, A):
        root = A
        while root != self.parent[root]:
            root = self.parent[root]

        while A != root:
            old_parent = self.parent[A]
            self.parent[A] = root
            A = old_parent
        return(root)

    def union(self, A, B):
        root_A = self.find(A)
        root_B = self.find(B)
        if root_A == root_B:
            return(False)

        if self.size[root_A] < self.size[root_B]:
            self.parent[root_A] = root_B
            self.size[root_B] += self.size[root_A]
        else:
            self.parent[root_B] = root_A
            self.size[root_A] += self.size[root_B]

        return(True)


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        R = len(grid)
        C = len(grid[0])
        dsu = UnionFind(R * C)

        def encode(r, c):
            return(r * C + c)

        for r in range(R):
            for c in range(C):
                if c + 1 < C and grid[r][c] == grid[r][c + 1]:
                    if not dsu.union(encode(r, c), encode(r, c + 1)):
                        return(True)
                if r + 1 < R and grid[r][c] == grid[r + 1][c]:
                    if not dsu.union(encode(r, c), encode(r + 1, c)):
                        return(True)

        return(False)
