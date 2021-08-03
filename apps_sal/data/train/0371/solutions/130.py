class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        # build graph of bus_stop: routes

        graph = {}
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                if routes[i][j] not in graph:
                    graph[routes[i][j]] = set()
                graph[routes[i][j]].add(i)

        visited_bus_stops = set()
        queue = []
        # initialize queue with the initial bus stop
        queue.append(S)
        visited_bus_stops.add(S)
        # for route in graph[S]:
        #     for bus_stop in routes[route]:
        #         queue.append(bus_stop)
        #         visited_bus_stops.add(bus_stop)

        distance = 0
        while queue:
            length = len(queue)
            for i in range(length):
                bus_stop = queue.pop(0)
                if bus_stop == T:
                    return distance

                for route in graph[bus_stop]:
                    for stop in routes[route]:
                        if stop not in visited_bus_stops:
                            queue.append(stop)
                            visited_bus_stops.add(stop)

            distance += 1

        return -1
