from collections import defaultdict


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        graph = defaultdict(list)
        for idx, route in enumerate(routes):
            for node in route:
                graph[node].append(idx)
        visited_node = set([S])
        visited_route = [0 for _ in range(len(routes))]
        queue = [(idx, 0) for idx in graph[S]]
        for idx, _ in queue:
            visited_route[idx] = 1
        while queue:
            id, depth = queue.pop(0)
            new_nodes = set(routes[id]) - visited_node
            visited_node = visited_node | new_nodes
            for node in new_nodes:
                if node == T:
                    return depth + 1
                for idx in graph[node]:
                    if visited_route[idx] == 0:
                        visited_route[idx] = 1
                        queue.append((idx, depth + 1))
        return -1 if S != T else 0
