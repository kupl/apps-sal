import heapq


class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        minHeap = []
        maxHeap = []
        zipped = list(zip(wage, quality))
        zipped = sorted(zipped, key=lambda x: x[0] / x[1])
        minCost = float('inf')
        totalQuality = 0
        for i in range(len(zipped)):
            curRatio = zipped[i][0] / zipped[i][1]
            if len(minHeap) < K:
                heapq.heappush(minHeap, (-zipped[i][1], zipped[i][0]))
                totalQuality += zipped[i][1]
            else:
                heapq.heappush(maxHeap, (zipped[i][1], zipped[i][0]))
                while curRatio * maxHeap[0][0] < curRatio * minHeap[0][0] * -1:
                    maxTop = heapq.heappop(maxHeap)
                    minTop = heapq.heappop(minHeap)
                    heapq.heappush(minHeap, (-maxTop[0], maxTop[1]))
                    heapq.heappush(maxHeap, (-minTop[0], minTop[1]))
                    totalQuality = totalQuality + minTop[0]
                    totalQuality += maxTop[0]
            if len(minHeap) == K and totalQuality * curRatio < minCost:
                minCost = totalQuality * curRatio
        return minCost
