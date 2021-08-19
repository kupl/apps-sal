class Solution:

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        heap = []
        stop = 0
        dist = startFuel
        for (d, g) in stations:
            if dist >= target:
                return stop
            while heap and dist < d:
                gas = heapq.heappop(heap)
                dist += -gas
                stop += 1
            if dist < d:
                return -1
            heapq.heappush(heap, -g)
        if dist >= target:
            return stop
        while heap:
            g = heapq.heappop(heap)
            stop += 1
            dist += -g
            if dist >= target:
                return stop
        return -1
