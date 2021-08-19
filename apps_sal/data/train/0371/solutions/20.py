class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        routes = [set(r) for r in routes]
        graph = collections.defaultdict(set)
        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                if routes[i].intersection(routes[j]):
                    graph[i].add(j)
                    graph[j].add(i)
        (seen, end) = (set(), set())
        for (i, x) in enumerate(routes):
            if S in x:
                seen.add(i)
            if T in x:
                end.add(i)
        q = [(n, 1) for n in seen]
        seen = set()
        for (n, d) in q:
            if n in end:
                return d
            for x in graph[n]:
                if x not in seen:
                    seen.add(x)
                    q.append((x, d + 1))
        return -1
