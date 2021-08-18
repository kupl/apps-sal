class Solution:
    def numBusesToDestination(self, routes, S, T):
        to_routes = collections.defaultdict(set)
        for route, stops in enumerate(routes):
            for s in stops:
                to_routes[s].add(route)
        bfs = [(S, 0)]
        seen = set([S])
        for stop, bus in bfs:
            if stop == T:
                return bus
            for i in to_routes[stop]:
                for j in routes[i]:
                    if j not in seen:
                        bfs.append((j, bus + 1))
                        seen.add(j)
                routes[i] = []
        return -1
