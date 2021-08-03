class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        queue = collections.deque()
        routes = list(map(set, routes))
        graph = collections.defaultdict(set)
        visited, targets = set(), set()
        for i in range(len(routes)):
            if S in routes[i]:  # possible starting route number
                visited.add(i)
                queue.append((i, 1))  # enqueue
            if T in routes[i]:  # possible ending route number
                targets.add(i)
            for j in range(i + 1, len(routes)):
                if routes[j] & routes[i]:  # set intersection to check if route_i and route_j are connected
                    graph[i].add(j)
                    graph[j].add(i)
        while queue:
            cur, depth = queue.popleft()
            if cur in targets:
                return depth
            for nxt in graph[cur]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, depth + 1))
        return -1
