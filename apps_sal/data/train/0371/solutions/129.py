class Solution:

    def numBusesToDestination(self, routes, S, T):
        to_routes = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                to_routes[j].add(i)
        bfs = collections.deque([(S, 0)])
        seen = set([S])
        while bfs:
            for _ in range(len(bfs)):
                stop, bus = bfs.popleft()
                if stop == T:
                    return bus
                for i in to_routes[stop]:
                    for j in routes[i]:
                        if j in seen:
                            continue
                        bfs.append((j, bus + 1))
                        seen.add(j)
        return -1
