class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        dic_stops = collections.defaultdict(set)
        for i, stops in enumerate(routes):
            for s in stops:
                dic_stops[s].add(i)
        visited_stops = set([S])
        visited_buses = set()
        queue = collections.deque([(S, 1)])
        while queue:
            stop, cnt = queue.popleft()
            for bus in dic_stops[stop]:
                if bus not in visited_buses:
                    visited_buses.add(bus)
                    for s in routes[bus]:
                        if s not in visited_stops:
                            if s == T:
                                return cnt
                            visited_stops.add(s)
                            queue.append((s, cnt + 1))
        return -1
