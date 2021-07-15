class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        stop = {}
        for i in range(len(routes)):
            for s in routes[i]:
                if s not in stop:
                    stop[s] = set()
                stop[s].add(i)
        stack = [(S, 0)]
        visited = set([S])
        while stack:
            node, level = stack.pop(0)
            for bus in stop[node]:
                for s in set(routes[bus]) - visited:
                    if s == T:
                        return level + 1
                    stack.append((s, level + 1))
                    visited.add(s)
        return -1
