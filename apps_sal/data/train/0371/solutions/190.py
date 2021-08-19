class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        (md, que, visited, changes) = (collections.defaultdict(set), collections.deque(), set(), {})
        for (b, r) in enumerate(routes):
            for s in r:
                md[s].add(b)
        if S not in md or T not in md:
            return -1
        if S == T:
            return 0
        for b in md[S]:
            for stop in routes[b]:
                que.append((stop, b, 1))
                changes[stop, b] = 1
        while que:
            (stop, bus, times) = que.popleft()
            if stop == T:
                return times
            for b in md[stop]:
                if bus != b:
                    for stop in routes[b]:
                        if (stop, bus) in changes and changes[stop, bus] > 1 + times:
                            que.append((stop, bus, 1 + times))
                            changes[stop, bus] = 1 + times
                        elif (stop, bus) not in changes:
                            changes[stop, bus] = 1 + times
                            que.append((stop, bus, 1 + times))
                    routes[b] = []
        return -1
