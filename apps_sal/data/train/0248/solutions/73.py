class Solution:

    def containsCycle(self, grid: List[List[str]]) -> bool:
        (m, n) = (len(grid), len(grid[0]))
        uf = {(i, j): (i, j) for i in range(m) for j in range(n)}

        def find(pos):
            if pos != uf[pos]:
                uf[pos] = find(uf[pos])
            return uf[pos]

        def union(pos1, pos2):
            root1 = find(pos1)
            root2 = find(pos2)
            if root1 != root2:
                uf[root1] = root2
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0 and (find((i - 1, j)) == find((i, j - 1))) and (grid[i][j] == grid[i - 1][j] == grid[i][j - 1]):
                    return True
                if i > 0 and grid[i][j] == grid[i - 1][j]:
                    union((i, j), (i - 1, j))
                if j > 0 and grid[i][j] == grid[i][j - 1]:
                    union((i, j), (i, j - 1))
        return False
