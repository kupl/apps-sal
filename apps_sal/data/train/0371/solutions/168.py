class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        adj_list = collections.defaultdict(set)
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                adj_list[routes[i][j]].add(i)
        queue = collections.deque([(S, 0)])
        visited = set()
        visited.add(S)
        while queue:
            node, taken = queue.popleft()
            if node == T:
                return taken
            for i in adj_list[node]:
                for j in routes[i]:
                    if j not in visited:
                        visited.add(j)
                        queue.append((j, taken + 1))
            routes[i] = []
        return -1
