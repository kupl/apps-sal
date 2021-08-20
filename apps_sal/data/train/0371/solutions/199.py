class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        stops = defaultdict(list)
        for (r, s) in enumerate(routes):
            for i in s:
                stops[i].append(r)
        (q, buses, been) = (deque([S]), [0] * len(routes), set())
        transfers = 0
        while q:
            size = len(q)
            for _ in range(size):
                i = q.popleft()
                if i == T:
                    return transfers
                for r in stops[i]:
                    if buses[r]:
                        continue
                    buses[r] = 1
                    for s in routes[r]:
                        if s in been:
                            continue
                        been.add(s)
                        q.append(s)
            transfers += 1
        return -1
