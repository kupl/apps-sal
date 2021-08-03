class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:

        if S == T:
            return 0
        q = [[S, 0]]
        d = defaultdict(set)
        for i, r in enumerate(routes):
            for e in r:
                d[e].add(i)
        visited = {}
        visited[S] = True
        while q:
            curr, step = q.pop(0)
            if curr == T:
                return step
            for e in d[curr]:
                for j in routes[e]:
                    if j not in visited:
                        visited[j] = None
                        q.append([j, step + 1])
                d[e] = []
        return -1
