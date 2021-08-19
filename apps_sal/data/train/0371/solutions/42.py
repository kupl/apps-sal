class Solution(object):

    def numBusesToDestination(self, routes, S, T):
        if S == T:
            return 0
        to_routes = collections.defaultdict(set)
        for (i, route) in enumerate(routes):
            for j in route:
                to_routes[j].add(i)
        bfs = [(S, 0)]
        for (stop, bus) in bfs:
            for i in to_routes[stop]:
                for j in routes[i]:
                    if j == T:
                        return bus + 1
                    bfs.append((j, bus + 1))
                routes[i] = []
        return -1
