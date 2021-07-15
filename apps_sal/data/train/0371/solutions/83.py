class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S==T:
            return 0
        n=len(routes)
        stop_bus=defaultdict(list)
        for bus,route in enumerate(routes):
            for stop in route:
                stop_bus[stop].append(bus)
        graph=[[] for _ in range(n)]
        for bus,route in enumerate(routes):
            for stop in route:
                buses=stop_bus[stop]
                for nei in buses:
                    if nei!=bus:
                        graph[bus].append(nei)
                        graph[nei].append(bus)
        start=set(stop_bus[S])
        end=set(stop_bus[T])
        if start.intersection(end):
            return 1
        for s in start:
            visited=start.copy()
            q=deque([(s, 1)])
            while q:
                cur, l = q.popleft()
                for nei in graph[cur]:
                    if nei not in visited:
                        if nei in end:
                            return l+1
                        visited.add(nei)
                        q.append((nei, l+1))
        return -1
                        

