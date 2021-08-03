from math import inf


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        rec = [[False] * n for _ in range(m)]
        res = inf

        def is_avail(r, c, k):
            return all(not rec[i][j] for i in range(r, r + k)
                       for j in range(c, c + k))

        def update(r, c, k, val):
            for i in range(r, r + k):
                for j in range(c, c + k):
                    rec[i][j] = val

        def dfs(r, c, cnt):
            nonlocal res
            if r == m:
                res = min(res, cnt)
                return

            if c == n:
                dfs(r + 1, 0, cnt)
                return

            if rec[r][c]:
                dfs(r, c + 1, cnt)
                return

            if cnt >= res:
                return

            max_tile = min(m - r, n - c)
            for k in range(max_tile, 0, -1):
                if is_avail(r, c, k):
                    update(r, c, k, True)
                    dfs(r, c + k, cnt + 1)
                    update(r, c, k, False)

        dfs(0, 0, 0)
        return res
