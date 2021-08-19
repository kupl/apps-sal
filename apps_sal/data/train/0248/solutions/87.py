class Solution:

    def containsCycle(self, g: List[List[str]]) -> bool:
        r = len(g)
        c = len(g[0])
        cc = {}

        def root(x):
            if cc[x] != x:
                cc[x] = root(cc[x])
            return cc[x]

        def join(x, y):
            rx = root(x)
            ry = root(y)
            if rx != ry:
                cc[rx] = ry
            return rx != ry
        for i in range(r):
            for j in range(c):
                cc[i, j] = (i, j)
        for i in range(r):
            for j in range(c):
                for (di, dj) in [[0, 1], [1, 0]]:
                    (ni, nj) = (i + di, j + dj)
                    if 0 <= ni < r and 0 <= nj < c and (g[i][j] == g[ni][nj]):
                        if not join((i, j), (ni, nj)):
                            return True
        return False
