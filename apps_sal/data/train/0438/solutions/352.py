

class Solution:
    def findLatestStep(self, a: List[int], m: int) -> int:

        n = len(a)

        c = Counter()
        par = {}
        sz = {}

        def add(u):

            c[1] += 1
            sz[u] = 1
            par[u] = u

        def merge(u, v):

            ru = find(u)
            rv = find(v)

            if ru != rv:

                c[sz[ru]] -= 1
                c[sz[rv]] -= 1
                c[sz[ru] + sz[rv]] += 1

                par[rv] = ru
                sz[ru] += sz[rv]

        def find(u):

            if par[u] != u:
                par[u] = find(par[u])

            return par[u]

        ret = -1

        for i, x in zip(list(range(1, n + 1)), a):

            add(x)

            if x - 1 in par:
                merge(x - 1, x)

            if x + 1 in par:
                merge(x + 1, x)

            if c[m]:
                ret = i

        return ret
