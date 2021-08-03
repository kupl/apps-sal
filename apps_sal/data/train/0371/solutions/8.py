class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        res = 0
        routeDones = set()
        stations = {S}
        while T not in stations:
            newStations = set()
            for i, route in enumerate(routes):
                if i in routeDones or len(stations.intersection(set(route))) == 0:
                    continue  # case only continue?
                newStations = newStations.union(set(route) - stations)
                routeDones.add(i)
            if len(newStations) == 0:
                return -1
            res += 1
            stations = stations.union(newStations)

        return res
