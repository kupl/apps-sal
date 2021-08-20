class Solution:

    def getKth(self, lo: int, hi: int, z: int) -> int:
        d = {}

        def dfs(k):
            if k == 1:
                return
            elif k % 2 == 0:
                c[0] += 1
                dfs(k // 2)
            else:
                c[0] += 1
                dfs(3 * k + 1)
        for i in range(lo, hi + 1):
            c = [0]
            dfs(i)
            d[i] = c[0]
        d = sorted(list(d.items()), key=lambda g: g[1])
        return d[z - 1][0]
