class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        # Builds graph.
        graph = collections.defaultdict(list)  # Don't use set. See below.
        for bus, stops in enumerate(routes):
            bus = -bus - 1  # To avoid conflict with the stops.

            # `set.update` consumes extra memory, so a `list` is used instead.
            graph[bus] = stops
            for s in stops:
                graph[s].append(bus)

        # Does BFS.
        dq = collections.deque()
        dq.append((S, 0))
        seen = set([S])
        while dq:
            node, depth = dq.popleft()
            for adj in graph[node]:
                if adj in seen:
                    continue
                if adj == T:
                    return depth
                # If `adj` < 0, it's a bus, so we add 1 to `depth`.
                dq.append((adj, depth + 1 if adj < 0 else depth))
                seen.add(adj)
        return -1
