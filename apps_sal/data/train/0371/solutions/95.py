class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        # want a graph such that buses with something in common are neighbors
        # then can just check if desired stop in the stop set, then return the level of a bfs traversal
        # queue would just be then initally all bus with S in them, can trivally return 1 I believe

        # O(n**2)
        # the question is how to construct a graph quickly, what is the point if the graph construction takes O(n**3) or worse?
        # especially with the shit with routes[i].length being ridiculous
        # iterate through i
        # iterate through routes[i]
        # add all buses as neighbors? That's pretty awful construction

        if S == T:
            return 0
        routes = [set(j) for j in routes]
        # looks like triple iteration will work jesus
        graph = {}

        for bus, route in enumerate(routes):
            graph.setdefault(bus, [])

            for other_bus in range(bus + 1, len(routes)):

                if any(r in routes[other_bus] for r in route):
                    graph[bus].append(other_bus)
                    graph.setdefault(other_bus, [])
                    graph[other_bus].append(bus)
        level = 1
        queue = [i for i in range(len(routes)) if S in routes[i]]
        seen = set()
        for bus in queue:
            seen.add(bus)
        while queue:
            new_queue = []
            for bus in queue:
                if T in routes[bus]:
                    return level
                for neighbor_bus in graph[bus]:
                    if neighbor_bus not in seen:
                        seen.add(neighbor_bus)
                        new_queue.append(neighbor_bus)
            queue = new_queue
            level += 1

        return -1
