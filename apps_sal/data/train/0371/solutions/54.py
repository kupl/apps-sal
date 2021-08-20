class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int):
        graph = collections.defaultdict(list)
        for i in range(len(routes)):
            for route in routes[i]:
                graph[route].append(i)
        q = collections.deque([(S, 0)])
        visited = set()
        while q:
            (cur_stop, out) = q.popleft()
            if cur_stop == T:
                return out
            for bus in graph[cur_stop]:
                if bus not in visited:
                    visited.add(bus)
                    for stop in routes[bus]:
                        q.append((stop, out + 1))
        return -1
