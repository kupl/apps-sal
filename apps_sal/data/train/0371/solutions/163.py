class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        graph = collections.defaultdict(set)

        for route in routes:
            for stop in set(route):
                graph[stop].update(route)

        queue = [(S, 0)]
        visited = {S}

        while queue:
            stop, dist = queue.pop(0)
            if stop == T:
                return dist
            for next_stop in graph[stop]:
                if next_stop not in visited:
                    queue.append((next_stop, dist + 1))
                    visited.add(next_stop)

        return -1
