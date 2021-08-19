from collections import defaultdict


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        routes = [set(x) for x in routes]

        stops = defaultdict(list)
        for i in range(len(routes)):
            for s in routes[i]:
                stops[s].append(i)

        # bfs
        curr_layer = [i for i, x in enumerate(routes) if S in x]
        next_layer = []
        num_routes = 1
        seen = set(curr_layer)

        while curr_layer:
            for i in curr_layer:

                if T in routes[i]:
                    return num_routes

                for j in routes[i]:
                    for k in stops[j]:
                        if k not in seen:
                            seen.add(i)
                            next_layer.append(k)

            curr_layer = next_layer
            next_layer = []
            num_routes += 1

        return -1
