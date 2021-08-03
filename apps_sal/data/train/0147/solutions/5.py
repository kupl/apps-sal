import heapq


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        bestTeamHeap = []
        heapSum = 0
        bestTeamScore = 0
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            heapq.heappush(bestTeamHeap, s)
            heapSum += s
            if len(bestTeamHeap) > k:
                heapSum -= heapq.heappop(bestTeamHeap)
            bestTeamScore = max(bestTeamScore, e * heapSum)
        return bestTeamScore % (10 ** 9 + 7)
