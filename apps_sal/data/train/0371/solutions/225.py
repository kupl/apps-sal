class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        stops = collections.defaultdict(set)
        reachable = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stops[stop].add(i)
                for j in stops[stop]:
                    reachable[i].add(j)
                    reachable[j].add(i)

        target_routes = stops[T]
        queue = collections.deque(stops[S])
        buses = 1
        reached = stops[S]
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                route = queue.popleft()
                if route in target_routes:
                    return buses
                for other_route in reachable[route]:
                    if other_route not in reached:
                        reached.add(other_route)
                        queue.append(other_route)
            buses += 1
        return -1
