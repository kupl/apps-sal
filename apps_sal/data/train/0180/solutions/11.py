class Solution:

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        q = []
        extent = startFuel
        ans = 0
        for i in range(len(stations)):
            if extent >= target:
                return ans
            (loc, fuel) = stations[i]
            print((i, loc, extent))
            while q and loc > extent:
                extent += -heapq.heappop(q)
                ans += 1
            if loc > extent:
                return -1
            heapq.heappush(q, -fuel)
        while q and extent < target:
            extent += -heapq.heappop(q)
            ans += 1
        if extent >= target:
            return ans
        else:
            return -1
