class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        graph = collections.defaultdict(list)
        for i, j in enumerate(routes):
            for stops in j:
                graph[stops].append(i)

        q = collections.deque(graph[S])
        visited = set()
        steps = 0
        while q:
            temp = []

            for bus in q:
                if bus in visited:
                    continue
                visited.add(bus)
                for r in routes[bus]:
                    if r == T:
                        return steps + 1
                    for b in graph[r]:
                        if b not in visited:
                            temp.append(b)
            q = temp
            steps += 1
        return -1
