class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        busDict = defaultdict(set)
        for (i, route) in enumerate(routes):
            for stop in route:
                busDict[stop].add(i)
        visited = set()
        queue = deque([S])
        res = 0
        while queue:
            leng = len(queue)
            res += 1
            for _ in range(leng):
                curr = queue.popleft()
                for bus in busDict[curr]:
                    if bus not in visited:
                        visited.add(bus)
                        if T in routes[bus]:
                            return res
                        queue.extend(routes[bus])
        return -1
