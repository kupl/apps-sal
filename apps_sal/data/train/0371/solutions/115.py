class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        visited = set()
        stop_bus = collections.defaultdict(list)
        for i in range(len(routes)):
            for stop in routes[i]:
                stop_bus[stop].append(i)
        # print(stop_bus)
        stops = collections.deque([(S, 0, 0)])
        
        while stops:
            cur_stop, n, taken = stops.popleft()
            # print(cur_stop, n, taken)
            if cur_stop == T:
                return n
            
            if cur_stop not in visited:
                next_stop = set()
                visited.add(cur_stop)
                for bus in stop_bus[cur_stop]:
                    # print(bus, taken, bus+1&taken)
                    if pow(2, bus) & taken == 0:  # never take the bus before
                        for stop in routes[bus]:
                            if stop in next_stop:
                                continue
                            next_stop.add(stop)
                            stops.append((stop, n+1, taken | pow(2, bus)))
        return -1
