class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        stop_to_bus = collections.defaultdict(set)
        bus_to_bus = {i: [] for i in range(len(routes))}

        # end_bus_q = collections.deque([])
        for bus, route in enumerate(routes):
            for stop in route:
                stop_to_bus[stop].add(bus)
        # print(stop_to_bus, init_bus_q)
        q = collections.deque(stop_to_bus[S])

        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                if len(set(routes[i]) & set(routes[j])) > 0:
                    bus_to_bus[i].append(j)
                    bus_to_bus[j].append(i)
        steps = 1
        visited = [False] * len(routes)
        # print(visited)
        while q:
            size = len(q)
            for _ in range(size):
                bus = q.popleft()
                # print(bus)
                visited[bus] = True
                if bus in stop_to_bus[T]:
                    return steps
                for nb in bus_to_bus[bus]:
                    if visited[nb]:
                        continue
                    q.append(nb)
            steps += 1
        return -1
