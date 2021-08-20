class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if not routes:
            return -1
        smap = defaultdict(set)
        for (bus, stops) in enumerate(routes):
            for stop in stops:
                smap[stop].add(bus)
        stack = [(S, 0)]
        visited_stop = set()
        while stack:
            (cur_stop, depth) = stack.pop(0)
            if T == cur_stop:
                return depth
            for bus in list(smap[cur_stop]):
                for stop in routes[bus]:
                    if stop not in visited_stop and stop not in stack:
                        stack.append((stop, depth + 1))
                        visited_stop.add(stop)
        return -1
