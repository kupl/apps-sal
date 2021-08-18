class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        roots = {}

        def find(x):
            roots.setdefault(x, x)

            if roots[x] != x:
                roots[x] = find(roots[x])

            return roots[x]

        def union(x, y):
            roots[find(x)] = find(y)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i > 0:
                    union((i - 1, j, 2), (i, j, 0))

                if j > 0:
                    union((i, j - 1, 1), (i, j, 3))

                if grid[i][j] != '/':
                    union((i, j, 0), (i, j, 1))
                    union((i, j, 2), (i, j, 3))

                if grid[i][j] != '\\\\':
                    union((i, j, 0), (i, j, 3))
                    union((i, j, 1), (i, j, 2))

        return len(set(find(x) for x in list(roots.keys())))
