class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        routes = list(map(set, routes))
        graph = collections.defaultdict(set)
        for (i, e) in enumerate(routes):
            for j in range(i + 1, len(routes)):
                for node in e:
                    if node in routes[j]:
                        graph[i].add(j)
                        graph[j].add(i)
        (target, start) = (set(), set())
        visited = set()
        for i in range(len(routes)):
            if S in routes[i]:
                start.add(i)
                visited.add(i)
            if T in routes[i]:
                target.add(i)
        step = 1
        while start:
            nextlevel = set()
            for node in start:
                if node in target:
                    return step
                for neighbornode in graph[node]:
                    if neighbornode not in visited:
                        visited.add(neighbornode)
                        nextlevel.add(neighbornode)
            step += 1
            start = nextlevel
        return -1
