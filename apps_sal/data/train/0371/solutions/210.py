class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        
        stopbusmap = collections.defaultdict(set)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stopbusmap[stop].add(bus)
        queue = []
        for bus in stopbusmap[S]:
            queue.append((routes[bus], [bus]))

        length = 0
        while queue:
            length += 1
            stops, taken = queue.pop(0)
            for stop in stops:
                if stop == T:
                    return len(taken)
                else:
                    for nxt in stopbusmap[stop]:
                        if nxt not in taken:
                            queue.append((routes[nxt], taken+[nxt]))
        return -1
