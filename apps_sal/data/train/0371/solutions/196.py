class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        graph = collections.defaultdict(set)
        for (i, route) in enumerate(routes):
            for r in route:
                graph[r].add(i)
        queue = [[S, 0]]
        visited = set([S])
        for (stop, bus) in queue:
            if stop == T:
                return bus
            for i in graph[stop]:
                for j in routes[i]:
                    if j not in visited:
                        queue.append([j, bus + 1])
                        visited.add(j)
                routes[i].clear()
        return -1
