class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target: return 0
        heap = []
        for d, g in stations:
            heapq.heappush(heap, (-g, d))
        dist = startFuel
        stop = 0
        dist = startFuel
        tmp = []
        while heap:
            g, d = heapq.heappop(heap)
            if d <= dist:
                dist += -g
                if dist >= target:
                    return stop + 1
                for el in tmp:
                    heapq.heappush(heap, el)
                tmp = []
                stop += 1
            else:
                tmp.append((g, d))
        return -1
        
                
                
            
        
                

