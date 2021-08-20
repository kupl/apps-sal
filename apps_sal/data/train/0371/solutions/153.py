from collections import deque


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if not routes:
            return -1
        if T == S:
            return 0
        q = deque([])
        r = []
        res = 0
        visited = set()
        for (idx, route) in enumerate(routes):
            r.append(set(route))
            if S in r[-1]:
                q.append(idx)
                visited.add(idx)
        print(q)
        while q:
            newq = []
            res += 1
            for bus in q:
                if T in r[bus]:
                    return res
                for stop in r[bus]:
                    for (idx, route) in enumerate(r):
                        if stop in route and idx not in visited:
                            visited.add(idx)
                            newq.append(idx)
            q = newq
        return -1
