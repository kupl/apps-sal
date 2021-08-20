class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if not routes:
            return None
        if S == T:
            return 0
        stack = []
        visited = []
        for (i, bus) in enumerate(routes):
            if S in bus:
                stack.append((bus, 1))
                visited.append(i)
                if T in bus:
                    return 1
        while stack:
            (bus, level) = stack.pop(0)
            bus = set(bus)
            for (i, b) in enumerate(routes):
                if i in visited:
                    continue
                if len(bus & set(b)) > 0:
                    stack.append((b, level + 1))
                    visited.append(i)
                    if T in b:
                        return level + 1
        return -1
