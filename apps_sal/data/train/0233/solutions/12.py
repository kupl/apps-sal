class Solution:

    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        D = list(range(N * N * 4))
        res = [len(D)]

        def find(D, i):
            if D[i] == i:
                return i
            return find(D, D[i])

        def union(D, i, j):
            pi = find(D, i)
            pj = find(D, j)
            if pi == pj:
                return
            else:
                D[pi] = pj
                res[0] -= 1

        def idx(i, j, e):
            return (i * N + j) * 4 + e
        for i in range(N):
            for j in range(N):
                if i > 0:
                    union(D, idx(i - 1, j, 2), idx(i, j, 0))
                if j > 0:
                    union(D, idx(i, j - 1, 1), idx(i, j, 3))
                if grid[i][j] != '/':
                    union(D, idx(i, j, 0), idx(i, j, 1))
                    union(D, idx(i, j, 2), idx(i, j, 3))
                if grid[i][j] != '\\\\':
                    union(D, idx(i, j, 0), idx(i, j, 3))
                    union(D, idx(i, j, 1), idx(i, j, 2))
        return res[0]
