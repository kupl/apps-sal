class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        queue = collections.deque()
        dic_buses = collections.defaultdict(set)
        dic_stops = collections.defaultdict(set)
        visited = set()
        reachable = set()
        for (i, stops) in enumerate(routes):
            dic_buses[i] = set(stops)
            if S in dic_buses[i]:
                if T in dic_buses[i]:
                    return 1
                visited.add(i)
                reachable |= dic_buses[i]
                queue.append(i)
            for j in dic_buses[i]:
                dic_stops[j].add(i)
        bus_need = 2
        visited_stops = set()
        while queue:
            length = len(queue)
            for _ in range(length):
                bus = queue.popleft()
                for stop in dic_buses[bus]:
                    if stop in visited_stops:
                        continue
                    visited_stops.add(stop)
                    for b in dic_stops[stop]:
                        if b not in visited:
                            if T in dic_buses[b]:
                                return bus_need
                            queue.append(b)
            bus_need += 1
        return -1
