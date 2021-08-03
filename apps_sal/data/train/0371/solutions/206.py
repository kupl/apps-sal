
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        if len(routes) == 0:
            return -1

        routesets = []
        for route in routes:
            routesets.append(set(route))
            # print(routesets[-1])

        # This is all points where buses meet.
        intersections = set()
        for i in range(len(routesets) - 1):
            set1 = routesets[i]
            for j in range(i + 1, len(routesets)):
                set2 = routesets[j]
                intersections.update(set1.intersection(set2))
        intersections.add(S)
        intersections.add(T)

        # print(intersections)

        # This is all the routes at an intersection
        i_to_routes = collections.defaultdict(list)
        for i in intersections:
            for ridx, route in enumerate(routesets):
                if i in route:
                    i_to_routes[i].append(ridx)

        for route in routesets:
            route.intersection_update(intersections)

        # print(i_to_routes)

        heap = []
        hist = set([S])

        heapq.heappush(heap, (0, 0, S))

        while heap:
            n, _, loc = heapq.heappop(heap)

            if loc == T:
                return n

            for route_idx in i_to_routes[loc]:
                for edge in routesets[route_idx].difference(hist):
                    hist.add(edge)
                    heapq.heappush(heap, (n + 1, abs(edge - T), edge))

        return -1
