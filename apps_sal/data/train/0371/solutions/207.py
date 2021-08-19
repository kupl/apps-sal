class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        conn = collections.defaultdict(list)
        for (i, route) in enumerate(routes):
            for j in route:
                conn[j].append(i)
        bfs = collections.deque()
        bfs.append((S, 0))
        visited = set([S])
        seen = set()
        while bfs:
            (s, bus) = bfs.popleft()
            if s == T:
                return bus
            for i in conn[s]:
                if i not in seen:
                    for j in routes[i]:
                        if j not in visited:
                            visited.add(j)
                            bfs.append((j, bus + 1))
                    seen.add(i)
        return -1
