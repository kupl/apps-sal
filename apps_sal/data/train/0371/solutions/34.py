class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        N = len(routes)
        if S == T:
            return 0
        routes = list(map(set, routes))
        g = [set() for _ in range(N)]
        for (ii, r1) in enumerate(routes):
            for jj in range(ii + 1, N):
                r2 = routes[jj]
                if any([1 for kk in r2 if kk in r1]):
                    g[ii].add(jj)
                    g[jj].add(ii)
        (ss, tt) = (set(), set())
        for (ii, jj) in enumerate(routes):
            if S in jj:
                ss.add(ii)
            if T in jj:
                tt.add(ii)
        queue = [(ii, 1) for ii in ss]
        for (ii, jj) in queue:
            if ii in tt:
                return jj
            for kk in g[ii]:
                if kk not in ss:
                    ss.add(kk)
                    queue.append((kk, jj + 1))
        return -1
