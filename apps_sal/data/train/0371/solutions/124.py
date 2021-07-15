class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        connections = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                connections[stop].add(i)
        visited = set()
        queue = deque()
        queue.append(S)
        visited.add(S)
        res = 0
        while queue:
            n = len(queue)
            for i in range(n):
                cur_stop = queue.popleft()
                if cur_stop == T:
                    return res
                for j in connections[cur_stop]:
                    for next_stop in routes[j]:
                        if not next_stop in visited:
                            queue.append(next_stop)
                            visited.add(next_stop)
            res += 1
        return -1
