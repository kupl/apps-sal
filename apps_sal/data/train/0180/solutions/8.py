class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        if startFuel >= target:
            return 0
        
        from heapq import heapify, heappop, heappush
        
        dis = startFuel
        heap = []
        stations = stations[::-1] 
        while stations and stations[-1][0] <= dis:
            s = stations.pop()
            heap.append((-s[1], s[0]))
            
        heapify(heap)
        
        
        stops = 0
        
        while heap:
            
            most_fuel = heappop(heap)
            stops += 1
            dis += (-most_fuel[0])
            if dis >= target:
                return stops
            while stations and stations[-1][0] <= dis:
                s = stations.pop()
                heappush(heap, (-s[1], s[0]))
            
        return -1
            
            
        

