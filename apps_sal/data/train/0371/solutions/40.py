class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        graph = defaultdict(list)

        start = []
        end = set()
        for i in range(len(routes)):
            iset = set(routes[i])
            for j in range(i + 1, len(routes)):
                if any(r in iset for r in routes[j]):
                    graph[i].append(j)
                    graph[j].append(i)

            if S in iset:
                start.append(i)
            if T in iset:
                end.add(i)

        qu = deque(start)

        ret = 1
        visited = set()
        while qu:
            nextqu = deque()
            while qu:
                cur = qu.pop()

                if cur in end:
                    return ret

                if cur in visited:
                    continue
                visited.add(cur)

                for n in graph[cur]:
                    if n not in visited:
                        nextqu.append(n)

            qu = nextqu
            ret += 1

        return -1
