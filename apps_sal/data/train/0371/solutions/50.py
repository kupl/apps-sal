class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        g = defaultdict(list)
        q = []
        t = set()
        routes = list(map(set, routes))
        for (i, r1) in enumerate(routes):
            if S in r1:
                q.append((i, 1))
            if T in r1:
                t.add(i)
            for j in range(i + 1, len(routes)):
                r2 = routes[j]
                if any((s in r2 for s in r1)):
                    g[i].append(j)
                    g[j].append(i)
        seen = set(q)
        while q:
            (node, jumps) = q.pop(0)
            if node in t:
                return jumps
            for nxt in g[node]:
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, jumps + 1))
        return -1
