class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target: return 0
        heap = [] #record the reachable gas for now
        stop = 0 #total stops
        dist = startFuel #reachable distance
        for d, g in stations:
            if dist >= target: #if reach target, return
                return stop
            while heap and dist < d: #make sure we can reach current station by make minimum stops
                gas = heapq.heappop(heap)
                dist += -gas
                stop += 1
            if dist < d: #if not reachable, return -1
                return -1
            heapq.heappush(heap, (-g)) #add current gas to heap for future stop
        if dist >= target:
                return stop
        while heap: #add the rest gas in heap from max to min to reach the target
            g = heapq.heappop(heap)
            stop += 1
            dist += -g
            if dist >= target:
                return stop
        return -1
        
                
                
            
        
                

