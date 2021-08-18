class DSU:
    def __init__(self, N):
        self.pres = list(range(N))

    def setRoot(self, i, root):
        while self.pres[i] != root:
            t = self.pres[i]
            self.pres[i] = root
            i = t
        return

    def findRoot(self, i):
        root = i
        while root != self.pres[root]:
            root = self.pres[root]
        self.setRoot(i, root)
        return root

    def merge(self, i, j):
        root = self.findRoot(i)
        self.setRoot(j, root)


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def getPos(N, h, w, i):
            return N * 4 * h + 4 * w + i

        N = len(grid)
        NN4 = N * N * 4
        dsu = DSU(NN4)

        for h in range(N):
            for w in range(N):
                p = getPos(N, h, w, 0)
                pR = getPos(N, h, w + 1, 0)
                pD = getPos(N, h + 1, w, 0)
                pRD = getPos(N, h + 1, w + 1, 0)
                if h < N - 1:
                    dsu.merge(p + 2, pD + 0)
                if w < N - 1:
                    dsu.merge(p + 1, pR + 3)

        for h in range(N):
            for w in range(N):
                p = getPos(N, h, w, 0)
                if grid[h][w] == '/':
                    dsu.merge(p + 0, p + 3)
                    dsu.merge(p + 1, p + 2)
                elif grid[h][w] == '\\\\':
                    dsu.merge(p + 0, p + 1)
                    dsu.merge(p + 2, p + 3)
                else:
                    dsu.merge(p + 0, p + 1)
                    dsu.merge(p + 0, p + 2)
                    dsu.merge(p + 0, p + 3)

        return sum(dsu.findRoot(x) == x for x in range(NN4))
