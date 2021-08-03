import heapq


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        point = 0
        level = 0
        gas = startFuel
        if gas >= target:
            return level
        heap = []
        stations.append([target + 1, float('inf')])
        for pos, gas_add in stations:
            if gas >= pos:
                heapq.heappush(heap, -gas_add)
            else:
                while heap:
                    gasmin = heapq.heappop(heap)
                    gas -= gasmin
                    level += 1
                    if gas >= target:
                        return level
                    if gas >= pos:
                        heapq.heappush(heap, -gas_add)
                        break
        return -1
