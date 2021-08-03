class Solution:
    def containsCycle(self, g: List[List[str]]) -> bool:
        def find(u):
            if u != UF[u]:
                u = find(UF[u])
            return UF[u]
        UF, m, n = {}, len(g), len(g[0])
        for i in range(m):
            for j in range(n):
                u = (i, j)
                UF.setdefault(u, u)
                for x, y in [(i, j - 1), (i - 1, j)]:
                    if not (0 <= x < m and 0 <= y < n):
                        continue
                    if g[x][y] == g[i][j]:
                        v = (x, y)
                        UF.setdefault(v, v)
                        pu, pv = find(u), find(v)
                        if pu != pv:
                            UF[pv] = pu
                        else:
                            return True
        return False
