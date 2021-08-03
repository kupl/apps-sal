class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []
        queue = deque()
        i = 0
        num_stations = 0

        while startFuel < target:
            while i < len(stations) and startFuel >= stations[i][0]:
                heapq.heappush(heap, (-stations[i][1]))
                i += 1

            if not heap:
                return -1

            next_fuel = heapq.heappop(heap)
            startFuel -= next_fuel
            num_stations += 1

        return num_stations
