class Solution:
    # bfs
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:

        md, que, visited, changes = collections.defaultdict(set), collections.deque(), set(), {}

        # prre-processing, we can get dict m[1] = (0), m[2] = (0), m[7] = (0,1) ,etc
        # means for stop 7 , bus 0, and 1 can reach
        for b, r in enumerate(routes):
            for s in r:
                md[s].add(b)

        # S or T not reachable
        if S not in md or T not in md:
            return -1

        # if S and T are same, we don't even need to take bus
        if S == T:
            return 0

        for b in md[S]:
            for stop in routes[b]:
                # (2,0,0), (7,0,0)
                # (1,0,0) - means stop 1, bus 0, bus changes 0
                que.append((stop, b, 1))
                # changes[1,0] = 0, changes[2,0] = 0, changes[7,0] = 0
                # means for reach 1,2,7 we just 1 times of bus change
                # (take the first bus also count as 1 change)
                changes[stop, b] = 1

        while que:
            stop, bus, times = que.popleft()
            # already reach the Target
            if stop == T:
                return times
            for b in md[stop]:
                if bus != b:
                    for stop in routes[b]:
                        # if I already reached this stop by bus, but I used few times for change
                        if (stop, bus) in changes and changes[stop, bus] > 1 + times:
                            que.append((stop, bus, 1 + times))
                            # remember update the new times in cache
                            changes[stop, bus] = 1 + times
                        elif (stop, bus) not in changes:  # I never reached stop by this bus yet
                            changes[stop, bus] = 1 + times
                            que.append((stop, bus, 1 + times))
                        # else: if I reached stop by bus, but I changed more times than the record in cache,
                        # just prunning it
                    # this sentences improve the performance greatly
                    # the time is from 5000ms decrease to 260 ms
                    routes[b] = []

        return -1

    # dijkstra
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:

        md, heap, visited, changes = collections.defaultdict(set), [], set(), set()

        # prre-processing, we can get dict m[1] = (0), m[2] = (0), m[7] = (0,1) ,etc
        # means for stop 7 , bus 0, and 1 can reach
        for b, r in enumerate(routes):
            for s in r:
                md[s].add(b)

        # S or T not reachable
        if S not in md or T not in md:
            return -1

        # if S and T are same, we don't even need to take bus
        if S == T:
            return 0

        for b in md[S]:
            for stop in routes[b]:
                # for test case: [[1,2,7],[3,6,7]], 1, 6
                # we got (1,0,2), (1,0,7)
                # means from stop 1 to go to stop 2 and 7, we just need to take one bus (1 changes )
                heapq.heappush(heap, (1, b, stop))
                # changes[1,0] = 0, changes[2,0] = 0, changes[7,0] = 0
                # means for reach 1,2,7 we just 1 times of bus change
                # (take the first bus also count as 1 change)
                changes.add((stop, b))

        while heap:
            times, bus, stop = heapq.heappop(heap)
            # already reach the Target
            if stop == T:
                return times
            for b in md[stop]:
                if bus != b:
                    for stop in routes[b]:
                        if (stop, bus) not in changes:  # I never reached stop by this bus yet
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



