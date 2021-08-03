class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0

        if not stations:
            return -1

        steps = 0
        i = 0
        pq = []

        while startFuel < target:
            while i < len(stations) and stations[i][0] <= startFuel:
                heapq.heappush(pq, -stations[i][1])
                i += 1

            if not pq:
                return -1
            else:
                startFuel -= heapq.heappop(pq)
                steps += 1

        return steps
