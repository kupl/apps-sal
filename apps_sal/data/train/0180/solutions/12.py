class Solution:

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []
        idx = 0
        cur = startFuel
        res = 0
        while cur < target:
            while idx < len(stations) and cur >= stations[idx][0]:
                heapq.heappush(pq, -stations[idx][1])
                idx += 1
            if not pq:
                return -1
            cur -= heapq.heappop(pq)
            res += 1
        return res
