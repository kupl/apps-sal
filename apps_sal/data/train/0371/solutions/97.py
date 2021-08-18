class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:

        md, que, visited, changes = collections.defaultdict(set), collections.deque(), set(), {}

        for b, r in enumerate(routes):
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
            stop, bus, times = que.popleft()
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

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:

        md, heap, visited, changes = collections.defaultdict(set), [], set(), set()

        for b, r in enumerate(routes):
            for s in r:
                md[s].add(b)

        if S not in md or T not in md:
            return -1

        if S == T:
            return 0

        for b in md[S]:
            for stop in routes[b]:
                heapq.heappush(heap, (1, b, stop))
                changes.add((stop, b))

        while heap:
            times, bus, stop = heapq.heappop(heap)
            if stop == T:
                return times
            for b in md[stop]:
                if bus != b:
                    for stop in routes[b]:
                        if (stop, bus) not in changes:
                            changes.add((stop, bus))
                            heapq.heappush(heap, (1 + times, bus, stop))
        return -1

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:

        if S == T:
            return 0
        graph = collections.defaultdict(set)

        routes = list(map(set, routes))

        for k1, r1 in enumerate(routes):
            for k2 in range(k1 + 1, len(routes)):
                if any(stop in routes[k2] for stop in r1):
                    graph[k1].add(k2)
                    graph[k2].add(k1)

        seen, targets = set(), set()
        for k, r in enumerate(routes):
            if S in r:
                seen.add(k)
            if T in r:
                targets.add(k)

        que = [(node, 1) for node in seen]

        while que:
            node, depth = que.pop(0)
            if node in targets:
                return depth
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    que.append((nei, depth + 1))

        return -1
