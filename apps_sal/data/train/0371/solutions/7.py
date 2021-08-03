class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        toroute = collections.defaultdict(set)
        seen = {S}
        for i, stops in enumerate(routes):
            for j in stops:
                toroute[j].add(i)

        q = collections.deque([(S, 0)])
        while q:
            s, b = q.popleft()
            if s == T:
                return b
            for i in toroute[s]:
                for j in routes[i]:
                    if j not in seen:
                        seen.add(s)
                        q.append((j, b + 1))
                routes[i] = []

        return -1
