class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        stops = collections.defaultdict(list)
        for (i, route) in enumerate(routes):
            for stop in route:
                stops[stop].append(i)
        num_routes = len(routes)
        expanded = set()
        q = collections.deque()
        routes = [set(route) for route in routes]
        for route in stops[S]:
            q.append([route, 1])
            expanded.add(route)
        while q:
            (cur_route, buses_taken) = q.popleft()
            if T in routes[cur_route]:
                return buses_taken
            for stop in routes[cur_route]:
                for transfer_route in stops[stop]:
                    if transfer_route not in expanded:
                        expanded.add(transfer_route)
                        q.append([transfer_route, buses_taken + 1])
        return -1
