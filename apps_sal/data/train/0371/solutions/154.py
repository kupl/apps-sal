class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        hmap = collections.defaultdict(set)
        for i in range(len(routes)):
            for j in routes[i]:
                hmap[j].add(i)
        q = [(S, 0)]
        visited = set()
        visited.add(S)
        while q:
            (stop, buses) = q.pop(0)
            if stop == T:
                return buses
            for i in hmap[stop]:
                for j in routes[i]:
                    if j not in visited:
                        visited.add(j)
                        q.append((j, buses + 1))
        return -1
