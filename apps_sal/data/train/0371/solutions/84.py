from collections import defaultdict


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        adj_list = defaultdict(set)
        for (i, a) in enumerate(routes):
            for k in a:
                adj_list[k].add(i)
        q = [[S, 0]]
        visited = {}
        for (stop, path_len) in q:
            if stop == T:
                return path_len
            if visited.get(stop) == None:
                for route in adj_list[stop]:
                    for k in routes[route]:
                        q.append([k, path_len + 1])
                visited[stop] = True
                routes[route] = []
        return -1
