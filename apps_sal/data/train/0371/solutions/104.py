from collections import defaultdict, deque


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:

        if S == T:
            return 0

        mapping = defaultdict(list)
        routes_mapping = defaultdict(set)
        stations_in_route = {}

        seen = set()

        for i, bus in enumerate(routes):

            stations_in_route[i] = set(bus)

            for station in bus:

                if station in mapping:
                    new_mapping = set(mapping[station])
                    routes_mapping[i] = routes_mapping[i] | new_mapping

                    for b in mapping[station]:
                        routes_mapping[b].add(i)

                mapping[station].append(i)

        queue = deque(mapping[S])
        seen = set(mapping[S])

        buses = 1

        while queue:

            for _ in range(len(queue)):

                bus = queue.popleft()

                if T in stations_in_route[bus]:
                    return buses

                for next_route in routes_mapping[bus]:
                    if next_route not in seen:
                        seen.add(next_route)
                        queue.append(next_route)

            buses += 1

        return -1
