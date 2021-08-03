import math


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        grid = [[0 for _ in range(m)] for _ in range(n)]

        def try_place(i: int, j: int, l: int) -> bool:
            ok = True
            xb, yb = None, None
            for x in range(i, i + l):
                for y in range(j, j + l):
                    if grid[x][y] == 1:
                        ok = False
                        xb, yb = x, y
                        break
                    grid[x][y] = 1
                if not ok:
                    break
            if not ok:
                done = False
                for x in range(i, i + l):
                    for y in range(j, j + l):
                        if (x, y) == (xb, yb):
                            done = True
                            break
                        grid[x][y] = 0
                    if done:
                        break
            return ok

        def un_place(i: int, j: int, l: int):
            for x in range(i, i + l):
                for y in range(j, j + l):
                    grid[x][y] = 0

        def search(i: int, j: int, sofar: int, ans: list):
            if sofar >= ans[0]:
                return
            if j == m:
                ans[0] = min(ans[0], sofar)
                return
            if i == n:
                search(0, j + 1, sofar, ans)
                return
            if grid[i][j] == 1:
                search(i + 1, j, sofar, ans)
                return
            for l in reversed(range(1, min(n - i + 1, m - j + 1))):
                if try_place(i, j, l):
                    search(i + 1, j, sofar + 1, ans)
                    un_place(i, j, l)

        if len(grid) == len(grid[0]):
            return 1
        ans = [math.inf]
        search(0, 0, 0, ans)
        return ans[0]
