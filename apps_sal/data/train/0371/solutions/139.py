class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        def bfs():
            Q = [(S, 0)]
            seen = set()
            while Q:
                (curStop, depth) = Q.pop(0)
                if T == curStop:
                    return depth
                for bus in busAtStops[curStop]:
                    for stop in routes[bus]:
                        if stop not in seen:
                            seen.add(stop)
                            Q.append((stop, depth + 1))
            return -1
        busAtStops = defaultdict(list)
        for (i, r) in enumerate(routes):
            for stop in r:
                busAtStops[stop].append(i)
            routes[i] = set(routes[i])
        return bfs()
