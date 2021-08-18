class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:

        root = {}

        def find(x):
            root.setdefault(x, x)
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rx, ry = find(x), find(y)

            if rx != ry:
                root[ry] = find(rx)

        for i in range(len(grid)):
            for j in range(len(grid)):
                if i:
                    union((i - 1, j, 2), (i, j, 0))
                if j:
                    union((i, j - 1, 1), (i, j, 3))
                if grid[i][j] == '/':
                    union((i, j, 0), (i, j, 3))
                    union((i, j, 1), (i, j, 2))
                elif grid[i][j] == '\\\\':
                    union((i, j, 0), (i, j, 1))
                    union((i, j, 2), (i, j, 3))
                else:
                    union((i, j, 0), (i, j, 1))
                    union((i, j, 0), (i, j, 2))
                    union((i, j, 0), (i, j, 3))

        return len(set(map(find, list(root.keys()))))
