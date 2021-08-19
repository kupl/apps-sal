class DSU:

    def __init__(self, N):
        self.par = list(range(N))
        self.sz = [1] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        (xr, yr) = (self.find(x), self.find(y))
        if xr == yr:
            return False
        if self.sz[xr] < self.sz[yr]:
            (xr, yr) = (yr, xr)
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        self.sz[yr] = self.sz[xr]
        return True


class Solution:

    def containsCycle(self, A: List[List[str]]) -> bool:
        (R, C) = (len(A), len(A[0]))

        def encode(r, c):
            return r * C + c
        dsu = DSU(R * C)
        for r in range(R):
            for c in range(C):
                if c + 1 < C and A[r][c] == A[r][c + 1]:
                    if not dsu.union(encode(r, c), encode(r, c + 1)):
                        return True
                if r + 1 < R and A[r][c] == A[r + 1][c]:
                    if not dsu.union(encode(r, c), encode(r + 1, c)):
                        return True
        return False
