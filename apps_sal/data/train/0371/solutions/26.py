class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:

        if S == T:
            return 0

        graph = collections.defaultdict(list)

        for index, route in enumerate(routes):
            for stop in route:

                graph[stop].append(index)

        print(graph)
        queue = graph[S]
        visited = set()
        steps = 0

        while queue:
            temp = []
            for bus in queue:
                if bus in visited:
                    continue
                else:
                    visited.add(bus)
                    for stops in routes[bus]:
                        if stops == T:
                            return steps + 1
                        for buses in graph[stops]:
                            if buses not in visited:
                                temp.append(buses)

            queue = temp
            steps += 1

        return -1
