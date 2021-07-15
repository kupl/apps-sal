class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        if not stations:
            return -1
        import heapq
        queue = [-f for i,f in stations if i <= startFuel]
        heapq.heapify(queue)
        fuel = startFuel
        start = max([i for i in range(len(stations)) if stations[i][0] <= startFuel] + [-1]) + 1
        result = 0
        while queue and fuel < target:
            fuel -= heapq.heappop(queue)
            result += 1
            while start < len(stations) and fuel >= stations[start][0]:
                heapq.heappush(queue, -stations[start][1])
                start += 1
        return result if fuel >= target else -1
