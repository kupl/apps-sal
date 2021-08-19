class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        buses = collections.defaultdict(set)
        count = 0
        visited = set()
        for (i, route) in enumerate(routes):
            for stop in route:
                buses[stop].add(i)
        q = [(S, 0)]
        for (stop, count) in q:
            if stop == T:
                return count
            for bus in buses[stop]:
                if bus not in visited:
                    visited.add(bus)
                    for next_stop in routes[bus]:
                        if next_stop != stop:
                            q.append((next_stop, count + 1))
        return -1
