class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        stops = {}
        for i in range(len(routes)):
            for stop in routes[i]:
                if stop not in stops:
                    stops[stop] = [[i], False]
                else:
                    stops[stop][0].append(i)
        next_stops = deque([S])
        visited = [False for i in range(len(routes))]
        remaining = 1
        buses = 0
        while len(next_stops) > 0:
            cur = next_stops.popleft()
            remaining -= 1
            stops[cur][1] = True
            for r in stops[cur][0]:
                if not visited[r]:
                    for s in routes[r]:
                        if s == T:
                            return buses + 1
                        if not stops[s][1]:
                            stops[s][1] = True
                            next_stops.append(s)
                    visited[r] = True
            if remaining == 0:
                remaining = len(next_stops)
                buses += 1
        return -1
