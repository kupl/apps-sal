class Solution:

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations = [[0, 0]] + stations
        heap = [(0, 0, -startFuel)]
        seen = {}
        while heap:
            (stop, pos, fuel) = heappop(heap)
            pos = -pos
            fuel = -fuel
            if pos in seen and seen[pos] >= fuel:
                continue
            seen[pos] = fuel
            if stations[pos][0] + fuel >= target:
                return stop
            if pos + 1 < len(stations) and fuel >= stations[pos + 1][0] - stations[pos][0]:
                new_fuel = fuel - (stations[pos + 1][0] - stations[pos][0])
                heappush(heap, (stop + 1, -(pos + 1), -(new_fuel + stations[pos + 1][1])))
                heappush(heap, (stop, -(pos + 1), -new_fuel))
        return -1
