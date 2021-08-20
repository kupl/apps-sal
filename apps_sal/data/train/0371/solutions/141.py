from collections import defaultdict, deque


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        stop_to_bus = defaultdict(set)
        for (bus, stops) in enumerate(routes):
            for stop in stops:
                stop_to_bus[stop].add(bus)
        queue = deque([(S, 0)])
        seen = set([S])
        while queue:
            (stop, steps) = queue.popleft()
            if stop == T:
                return steps
            for bus in stop_to_bus[stop]:
                for next_stop in routes[bus]:
                    if next_stop not in seen:
                        seen.add(next_stop)
                        queue.append((next_stop, steps + 1))
        return -1
