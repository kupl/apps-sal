class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:

        m, n = len(grid), len(grid[0])
        root = {}
        size = {}

        def find(t):
            if root[t] != t:
                root[t] = find(root[t])
            return root[t]

        for i in range(m):
            for j in range(n):
                root[(i, j)] = (i, j)
                size[(i, j)] = 1

                if 0 <= i - 1 and grid[i - 1][j] == grid[i][j]:
                    top = (i - 1, j)
                    rt = find(top)
                    root[(i, j)] = rt
                    size[rt] += 1
                if 0 <= j - 1 and grid[i][j - 1] == grid[i][j]:
                    left = (i, j - 1)
                    rl = find(left)
                    root[(i, j)] = rl
                    size[rl] += 1
                if 0 <= i - 1 and 0 <= j - 1 and grid[i - 1][j] == grid[i][j] and grid[i][j - 1] == grid[i][j]:
                    rl = root[(i, j - 1)]
                    rt = root[(i - 1, j)]
                    if rl == rt:
                        return True
                    if size[rt] >= size[rl]:
                        root[rl] = rt
                        size[rt] += size[rl]
                    else:
                        root[rt] = rl
                        size[rl] += size[rt]
        return False
