class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        graph = collections.defaultdict(list)
        for i, stops in enumerate(routes):
            for stop in stops:
                graph[stop].append(i)

        q = graph[S]
        visited = set()
        steps = 0
        while q:
            tmp = []
            for bus in q:
                if bus in visited:
                    continue
                visited.add(bus)
                for stop in routes[bus]:
                    if stop == T:
                        return steps + 1
                    for bus2 in graph[stop]:
                        if bus2 not in visited:
                            tmp.append(bus2)

            q = tmp
            steps += 1
        return -1
