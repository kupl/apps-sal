class Solution:

    def regionsBySlashes(self, grid: List[str]) -> int:
        f = {}

        def find(x):
            if x not in f:
                f[x] = x
            elif f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def merge(x, y):
            (rx, ry) = (find(x), find(y))
            f[rx] = ry
        (rows, cols) = (len(grid), len(grid[0]) if grid else 0)
        for i in range(rows):
            for j in range(cols):
                cur = (i * cols + j) * 4
                (up, left) = (((i - 1) * cols + j) * 4, (i * cols + j - 1) * 4)
                (cl, cr, cd) = (cur + 3, cur + 1, cur + 2)
                (lr, ud) = (left + 1, up + 2)
                if grid[i][j] == '/':
                    merge(cur, cl)
                    merge(cr, cd)
                elif grid[i][j] == '\\\\':
                    merge(cur, cr)
                    merge(cl, cd)
                else:
                    merge(cur, cr)
                    merge(cl, cd)
                    merge(cur, cl)
                if i >= 1:
                    merge(cur, ud)
                if j >= 1:
                    merge(cl, lr)
        res = 0
        for i in range(rows):
            for j in range(cols):
                cur = (i * cols + j) * 4
                for dx in range(4):
                    if cur + dx == find(cur + dx):
                        res += 1
        return res
