class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        # BFS
        # The first part loop on routes and record stop to routes mapping in to_route.
        # The second part is general bfs. Take a stop from queue and find all connected route.
        # The hashset seen record all visited stops and we won't check a stop for twice.
        # We can also use a hashset to record all visited routes, or just clear a route after visit.

        to_routes = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                to_routes[j].add(i)
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
                routes[i] = []  # seen route
        return -1
