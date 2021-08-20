class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        import queue
        if S == T:
            return 0
        edge_dict = {}
        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                if i not in edge_dict:
                    edge_dict[i] = {}
                if j not in edge_dict:
                    edge_dict[j] = {}
                if len(set(routes[i]).intersection(set(routes[j]))) != 0:
                    edge_dict[i][j] = 1
                    edge_dict[j][i] = 1
        frontier = queue.SimpleQueue()
        seen = {}
        for i in range(len(routes)):
            if S in routes[i]:
                frontier.put((i, 1))
                seen[i] = 1
        while not frontier.empty():
            (node, dist) = frontier.get()
            if T in routes[node]:
                return dist
            neighbors = list(edge_dict[node].keys())
            for neighbor in neighbors:
                if neighbor not in seen:
                    seen[neighbor] = dist + 1
                    frontier.put((neighbor, dist + 1))
        return -1
