class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        num_buses = len(routes)
        bus_to_stop = defaultdict(set)
        for bus, stops in enumerate(routes):
            bus_to_stop[bus] = set(stops)

        def update_buses_used():
            for bus in range(num_buses):
                if bus in buses_used:
                    continue
                if stops_reached & bus_to_stop[bus]:
                    buses_used.add(bus)

        def update_stops_reached():
            for bus in buses_used:
                stops_reached.update(bus_to_stop[bus])

        buses_used = set()
        stops_reached = {S}
        pre_stop_count = 0
        bus_count = 0
        while len(stops_reached) > pre_stop_count:
            if T in stops_reached:
                return bus_count
            pre_stop_count = len(stops_reached)
            update_buses_used()
            update_stops_reached()
            bus_count += 1

        return -1

    def numBusesToDestination(self, routes, S, T):
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
                routes[i] = []
        return -1
