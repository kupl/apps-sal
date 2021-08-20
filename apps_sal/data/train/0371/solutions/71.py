class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        maps = {}
        for i in range(len(routes)):
            r = routes[i]
            for j in range(len(r)):
                if r[j] not in maps.keys():
                    maps[r[j]] = set()
                maps[r[j]].add(i)
        res = 0
        lens = len(routes)
        seenBus = [0] * lens
        seenStop = set()
        q = [S]
        res = 0
        while q:
            res += 1
            size = len(q)
            for i in range(size):
                stop = q.pop(0)
                for bus in maps[stop]:
                    if seenBus[bus] == 1:
                        continue
                    seenBus[bus] = 1
                    for s in routes[bus]:
                        if s == T:
                            return res
                        if s in seenStop:
                            continue
                        seenStop.add(s)
                        q.append(s)
        return -1
