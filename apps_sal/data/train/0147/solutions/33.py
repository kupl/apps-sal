from heapq import heappush, heappop
class Engineer:
    def __init__(self, speed, efficiency):
        self.speed = speed
        self.efficiency = efficiency
        
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = []
        for i in range(n):
            engineers.append(Engineer(speed[i], efficiency[i]))
        engineers.sort(key=lambda eng: eng.efficiency, reverse = True)
        minHeap = []
        maxPerform, sumOfSpeed = 0, 0
        for i, eng in enumerate(engineers):
            sumOfSpeed += eng.speed
            heappush(minHeap, [eng.speed, i,eng])
            if len(minHeap) > k:
                sumOfSpeed -= heappop(minHeap)[2].speed
            maxPerform = max(sumOfSpeed * eng.efficiency, maxPerform)
        
        return maxPerform % (10**9 + 7)

