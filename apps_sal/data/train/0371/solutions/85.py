class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        n = len(routes)
        graph = collections.defaultdict(list)
        sources = set()
        targets = set()
        for i in range(n):
            if S in routes[i]:
                sources.add(i)
            if T in routes[i]:
                targets.add(i)
            for j in range(i + 1, n):
                if set(routes[i]) & set(routes[j]):
                    graph[i].append(j)
                    graph[j].append(i)
        dist = 1
        seen = set()
        while sources:
            temp = set()
            for curr in sources:
                if curr in targets:
                    return dist
                for neighbor in graph[curr]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        temp.add(neighbor)
            sources = temp
            dist += 1
        return -1
