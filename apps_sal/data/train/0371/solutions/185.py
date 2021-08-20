class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        graph = collections.defaultdict(list)
        for (bus, stops) in enumerate(routes):
            bus = -bus - 1
            graph[bus] = stops
            for s in stops:
                graph[s].append(bus)
        dq = collections.deque()
        dq.append((S, 0))
        seen = {S}
        while dq:
            (node, depth) = dq.popleft()
            for adj in graph[node]:
                if adj in seen:
                    continue
                if adj == T:
                    return depth
                dq.append((adj, depth + 1 if adj < 0 else depth))
                seen.add(adj)
        return -1
