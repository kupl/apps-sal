class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target : return 0
        
        pq = []
        minStops = i = 0
        curr = startFuel
        
        while curr < target:
            while i < len(stations) and curr >= stations[i][0]:
                heapq.heappush(pq, -stations[i][1])
                i += 1
            if not pq: return -1
            curr += -heapq.heappop(pq)
            minStops +=1
        return minStops

