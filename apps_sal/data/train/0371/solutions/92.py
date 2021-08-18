class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        for i in range(len(routes)):
            routes[i] = set(routes[i])

        start_bus = set()
        end_bus = set()
        connections = collections.defaultdict(set)
        for i in range(len(routes)):
            busA = routes[i]

            if S in busA:
                start_bus.add(i)

            if T in busA:
                end_bus.add(i)

            for j in range(len(routes)):
                if i == j:
                    continue

                busB = routes[j]
                if len(busA & busB):
                    connections[i].add(j)

        if start_bus == end_bus:
            return 1 if S != T else 0

        S = list(start_bus)[0]
        T = list(end_bus)[0]

        first_hop = 1

        q = [(1, s) for s in start_bus]

        seen = set()

        ans = float('inf')
        while q:
            W, C = heapq.heappop(q)

            if C in end_bus:
                end_bus.remove(C)

                ans = min(ans, W)

                if not end_bus:
                    break

            if C in seen:
                continue

            seen.add(C)

            W += 1
            for i in connections[C]:
                if i not in seen:
                    heapq.heappush(q, (W, i))

        return -1 if ans == float('inf') else ans
