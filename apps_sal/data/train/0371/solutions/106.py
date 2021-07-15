class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        stop_to_bus = collections.defaultdict(list)
        for i in range(len(routes)):
            for stop in routes[i]:
                stop_to_bus[stop].append(i)
        bus_to_stop = routes
        
        queue = collections.deque([S])
        visited_bus = set()
        level = 0
        while queue:
            for _ in range(len(queue)):
                stop = queue.popleft()
                if stop == T:
                    return level
                for bus in stop_to_bus[stop]:
                    if bus in visited_bus:
                        continue
                    visited_bus.add(bus)
                    for next_stop in bus_to_stop[bus]:
                        queue.append(next_stop)
            level += 1
        return -1
