class Solution:

    def containsCycle(self, grid: List[List[str]]) -> bool:
        (R, C) = (len(grid), len(grid[0]))
        UF = {}

        def find(u):
            if UF[u] != u:
                UF[u] = find(UF[u])
            return UF[u]

        def union(u, v):
            UF.setdefault(u, u)
            UF.setdefault(v, v)
            UF[find(u)] = find(v)
        for i in range(R):
            for j in range(C):
                if i > 0 and grid[i][j] == grid[i - 1][j]:
                    if (i, j) in UF and (i - 1, j) in UF and (find((i, j)) == find((i - 1, j))):
                        return True
                    union((i, j), (i - 1, j))
                if j > 0 and grid[i][j] == grid[i][j - 1]:
                    if (i, j) in UF and (i, j - 1) in UF and (find((i, j)) == find((i, j - 1))):
                        return True
                    union((i, j), (i, j - 1))
        return False
