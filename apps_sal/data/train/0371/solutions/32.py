class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        num_buses = len(routes)
        bus_to_stop = defaultdict(set)
        stop_to_bus = defaultdict(set)
        for bus, stops in enumerate(routes):
            bus_to_stop[bus] = set(stops)
            for stop in stops:
                stop_to_bus[stop].add(bus)

        def update_buses_used():
            for bus in range(num_buses):
                if bus in buses_used:
                    continue
                if stops_reached & bus_to_stop[bus]:
                    buses_used.add(bus)

        def update_stops_reached(stops_reached):
            for bus in buses_used:
                stops_reached |= bus_to_stop[bus]

        buses_used = set()
        stops_reached = {S}
        pre_stop_count = 0
        bus_count = 0
        while len(stops_reached) > pre_stop_count:
            if T in stops_reached:
                return bus_count
            pre_stop_count = len(stops_reached)
            update_buses_used()
            update_stops_reached(stops_reached)
            bus_count += 1

        return -1
