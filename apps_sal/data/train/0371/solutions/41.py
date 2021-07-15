class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        stop_to_bus = collections.defaultdict(list)
        for bus,stops in enumerate(routes):
            for stop in stops:
                stop_to_bus[stop].append(bus)
        
        q = collections.deque([S])
        seen_bus = set()
        # seen_stop = set()
        step = -1
        while q:
            step += 1
            for _ in range(len(q)):
                stop = q.popleft()
                if stop == T:
                    return step
                for bus in stop_to_bus[stop]:
                    if bus in seen_bus:
                        continue
                    seen_bus.add(bus)
                    for next_stop in routes[bus]:
                        # if next_stop in seen_stop:
                        #     continue
                        q.append(next_stop)
                        # seen_stop.add(stop)
        return -1        
