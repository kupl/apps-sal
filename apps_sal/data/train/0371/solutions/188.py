class Solution:
    def numBusesToDestination(self, routes, S, T):
        if S == T:
            return 0
        queue = collections.deque()
        graph = collections.defaultdict(set)
        routes = list(map(set, routes))

        seen, targets = set(), set()

        for i in range(len(routes)):
            if S in routes[i]:
                seen.add(i)
                queue.append((i, 1))
            if T in routes[i]:
                targets.add(i)
            for j in range(i + 1, len(routes)):
                if routes[j] & routes[i]:
                    graph[i].add(j)
                    graph[j].add(i)

        while queue:
            cur, count = queue.popleft()
            if cur in targets:
                return count
            for nei in graph[cur]:
                if nei not in seen:
                    queue.append((nei, count + 1))
                    seen.add(nei)
        return -1
