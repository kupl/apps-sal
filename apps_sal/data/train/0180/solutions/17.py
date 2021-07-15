class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel>=target:
            return 0
        stations.sort(reverse=True)
        fuel=startFuel
        heap=[]
        out=0
        while stations:
            while stations and fuel>=stations[-1][0]:
                t,val=stations.pop()
                if t>=target:
                    return out
                heapq.heappush(heap,-val)
            if heap:
                fuel-=heapq.heappop(heap)
                out+=1
                if fuel>=target:
                    return out
            else:
                break
        while heap and fuel<target:
            fuel-=heapq.heappop(heap)
            out+=1
        if fuel<target:
            return -1
        return out
