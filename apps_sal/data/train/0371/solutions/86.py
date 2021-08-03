class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if not routes:
            return -1
        bus2stop = collections.defaultdict(set)
        stop2bus = collections.defaultdict(set)
        for bus, route in enumerate(routes):
            for stop in route:
                bus2stop[bus].add(stop)
                stop2bus[stop].add(bus)

        q = collections.deque()
        q.append((0, S))
        seen = set()
        seen.add(S)
        while q:
            hop, curStop = q.popleft()
            if curStop == T:
                return hop
            for bus in stop2bus[curStop]:
                for nxtStop in bus2stop[bus]:
                    if nxtStop not in seen:
                        seen.add(nxtStop)
                        q.append((hop + 1, nxtStop))

        return -1
