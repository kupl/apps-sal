class Node:
    def __init__(self):
        self.idx = None
        self.val = set()


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        is_t_present = False
        all_routes = []
        potential_starts = []
        graph = collections.defaultdict(list)

        for i, route in enumerate(routes):
            node = Node()
            node.idx = i
            node.val = set(route)
            if S in node.val:
                potential_starts.append([i, 1])
                if T in node.val:
                    return 1
            if T in node.val:
                is_t_present = True
            all_routes.append(node)

        if not is_t_present or not potential_starts:
            return -1

        for i in range(len(all_routes)):
            curr = all_routes[i]
            for j in range(i + 1, len(all_routes)):
                temp = all_routes[j]
                if curr.val & temp.val:
                    graph[i].append(j)
                    graph[j].append(i)

        dq = collections.deque(potential_starts)
        visited = set()
        while len(dq) > 0:
            idx, depth = dq.popleft()
            visited.add(idx)
            node = all_routes[idx]
            if T in node.val:
                return depth
            for nei in graph[idx]:
                if nei not in visited:
                    dq.append([nei, depth + 1])
        return -1
