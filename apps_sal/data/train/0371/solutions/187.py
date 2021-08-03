class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        # already at the destination
        if S == T:
            return 0

        # dictionary of busstops and buses
        # this maintains a dictionary of which bus routes fall on which bustops
        busDict = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                busDict[stop].add(i)

        # to avoid visiting the same bus route
        visited = set()
        # queue for traversing through bus stops.
        queue = deque([S])
        res = 0
        while queue:
            leng = len(queue)
            res += 1
            for _ in range(leng):

                curr = queue.popleft()

                # check which buses pass through the current bus stop
                for bus in busDict[curr]:
                    if bus not in visited:
                        visited.add(bus)

                        # check if this bus route contains the destination
                        if T in routes[bus]:
                            return res
                        queue.extend(routes[bus])
        return -1
