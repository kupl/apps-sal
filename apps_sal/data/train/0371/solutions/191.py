class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        routes = [set(stops) for stops in routes]

        taken = set()
        dq = collections.deque()

        neighbors = collections.defaultdict(list)

        for i in range(len(routes)):
            if S in routes[i]:
                dq.append(i)
                taken.add(i)
            for j in range(i):
                if routes[i].intersection(routes[j]):
                    neighbors[i].append(j)
                    neighbors[j].append(i)

        count = 1
        while dq:
            size = len(dq)
            for _ in range(size):
                bus = dq.popleft()
                if T in routes[bus]:
                    return count
                for nei in neighbors[bus]:
                    if nei not in taken:
                        dq.append(nei)
                        taken.add(nei)
            count += 1

        return -1
