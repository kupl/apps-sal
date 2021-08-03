import heapq


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stops = 0
        max_gas_heap = []
        can_drive_to = startFuel
        i = 0
        while can_drive_to < target:
            # push stations to heap
            while i < len(stations) and stations[i][0] <= can_drive_to:
                heapq.heappush(max_gas_heap, -stations[i][1])
                i += 1

            if not max_gas_heap:
                return -1
            can_drive_to -= heapq.heappop(max_gas_heap)
            stops += 1

        return stops
