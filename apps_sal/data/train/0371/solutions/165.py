class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        graph = [set() for _ in range(len(routes))]
        stops = defaultdict(list)
        q = set()
        ends = set()
        for i, route in enumerate(routes):
            for stop in route:
                for other in stops[stop]:
                    graph[i].add(other)
                    graph[other].add(i)

                stops[stop].append(i)
                if stop == S:
                    q.add(i)
                if stop == T:
                    ends.add(i)
        dist = 1
        seen = q.copy()
        while q:
            next_level = set()
            count = len(q)
            for route in q:
                if route in ends:
                    return dist

                for n in graph[route]:
                    if n not in seen:
                        next_level.add(n)
                        seen.add(n)

            q = next_level
            dist += 1

        return -1
