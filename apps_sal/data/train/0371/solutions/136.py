class Solution:

    def numBusesToDestination(self, routes, S, T):
        """toRoutes = collections.defaultdict(set)
        for i,route in enumerate(routes):
            for j in route:
                toRoutes[j].add(i)
        bfs = [(S, 0)]
        seen = set([S])
        for stop, bus in bfs:
            if stop == T:
                return bus 
            for idx in toRoutes[stop]:
                for nextStop in routes[idx]:
                    if nextStop not in seen:
                        seen.add(nextStop)
                        bfs.append((nextStop, bus+1))
                routes[idx] = []
        return -1"""
        toRoutes = collections.defaultdict(set)
        for (i, route) in enumerate(routes):
            for r in route:
                toRoutes[r].add(i)
        bfs = [(S, 0)]
        seen = set([S])
        'Example:\nInput: \nroutes = [[1, 2, 7], [3, 6, 7]]\nS = 1\nT = 6\nOutput: 2\nExplanation: \n        '
        for (stop, bus) in bfs:
            if stop == T:
                return bus
            for idx in toRoutes[stop]:
                for nextStop in routes[idx]:
                    if nextStop not in seen:
                        seen.add(nextStop)
                        bfs.append((nextStop, bus + 1))
        return -1
