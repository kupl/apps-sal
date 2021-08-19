class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        N = len(arr)
        par = [0] * N
        rank = [0] * N
        sz = [0] * N
        ops = {}
        for n in range(N):
            par[n] = n

        def find(u):
            if par[u] == u:
                return u
            par[u] = find(par[u])
            return par[u]

        def merge(u, v):
            (up, vp) = (find(u), find(v))
            if rank[up] < rank[vp]:
                par[up] = vp
                sz[vp] += sz[up]
                sz[up] = 0
            elif rank[vp] < rank[up]:
                par[vp] = up
                sz[up] += sz[vp]
                sz[vp] = 0
            else:
                par[up] = vp
                sz[vp] += sz[up]
                rank[vp] += 1
                sz[up] = 0
        snap = [0] * N
        last = -1
        for (p, n) in enumerate(arr):
            n -= 1
            snap[n] = 1
            sz[n] = 1
            mark = False
            if n - 1 >= 0 and snap[n - 1] == 1:
                p1 = find(n - 1)
                if p1 in ops:
                    del ops[p1]
                mark = True
                merge(n - 1, n)
            if n + 1 < N and snap[n + 1] == 1:
                p1 = find(n + 1)
                if p1 in ops:
                    del ops[p1]
                mark = True
                merge(n, n + 1)
            para = find(n)
            if sz[para] == m:
                ops[para] = 1
            if ops:
                last = p
        if last == -1:
            return -1
        return last + 1
