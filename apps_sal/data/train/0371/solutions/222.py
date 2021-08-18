class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if (S == T):
            return 0
        buses = collections.defaultdict(list)
        for i, bus in enumerate(routes):
            for stop in bus:
                buses[stop].append(i)
        q = [S]
        result = 0
        took = set()
        visited = set()
        visited.add(S)
        while (q):
            for i in range(len(q), 0, -1):
                now = q.pop(0)
                for bus in buses[now]:
                    if (bus not in took):
                        for route in routes[bus]:
                            if (route not in visited):
                                if (route == T):
                                    return result + 1
                                q.append(route)
                                visited.add(route)
                        took.add(bus)
            result += 1

        return -1
