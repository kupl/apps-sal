class Solution:
    def numBusesToDestination(self, bus_routes: List[List[int]], start: int, end: int) -> int:
        # return self.approach_2(bus_routes, start, end)
        if start == end:
            return 0
        on_stop = defaultdict(set)
        for i, route in enumerate(bus_routes):
            for stop in route:
                on_stop[stop].add(i)
        bfs = []
        bfs.append((start, 0))
        seen = set([start])
        for stop, bus_count in bfs:
            if stop == end:
                return bus_count
            for buses in on_stop[stop]:
                for stops in bus_routes[buses]:
                    if stops not in seen:
                        if stops == end:
                            return bus_count+1
                        seen.add(stops)
                        bfs.append((stops, bus_count+1))
                bus_routes[buses] = []
        return -1

    def approach_2(self, bus_routes, start, end):
        if start == end: return 0
        graph = defaultdict(set)
        bus_routes = list(map(set, bus_routes))
        start_set = set()
        end_set = set()
        for bus, stops in enumerate(bus_routes):
            for other_buses in range(bus+1, len(bus_routes)):
                other_bus_route = bus_routes[other_buses]
                if not other_bus_route.isdisjoint(stops):
                    graph[bus].add(other_buses)
                    graph[other_buses].add(bus)
        for bus,route in enumerate(bus_routes):
            if start in route: start_set.add(bus)
            if end in route: end_set.add(bus)

        queue = [(node, 1) for node in start_set]
        for bus, changes in queue:
            if bus in end_set: return changes
            for nei in graph[bus]:
                if nei not in start_set:
                    start_set.add(nei)
                    queue.append((nei, changes+1))
        return -1
    
    def approach_3(self, buses, start, end):
        on_stop = defaultdict(set)
        for bus, stops in enumerate(buses):
            for stop in stops:
                on_stop[stop].add(bus)
        bfs = [(start, 0)]
        seen = set()
        seen.add(start)
        for stop, dist in bfs:
            if stop == end:
                return dist
            for bus in on_stop[stop]:
                for stops in buses[bus]:
                    if end == start:
                        return dist+1
                    if stops not in seen:
                        seen.add(stops)
                        bfs.append((stops, dist+1))
        return -1


