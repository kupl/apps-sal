class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        bus_stops = {}
        untaken_bus, bfs_queue = set(), []
        for bus, stops in enumerate(routes):
            bus_stops[bus] = set(stops)
            if S in bus_stops[bus]:
                bfs_queue.append(bus)
                continue
            untaken_bus.add(bus)

        res = 1
        while bfs_queue:
            next_bfs_queue = []
            for bus in bfs_queue:
                if T in bus_stops[bus]:
                    return res
                for u_b in list(untaken_bus):
                    if bus_stops[u_b].intersection(bus_stops[bus]):
                        next_bfs_queue.append(u_b)
                        untaken_bus.remove(u_b)
            bfs_queue = next_bfs_queue
            res += 1
        return -1
