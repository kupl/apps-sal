class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = sorted(zip(speed, efficiency), key=lambda eng: eng[1], reverse=True)
        h = []
        res = 0
        speedSum = 0
        for s, e in engineers:
            heapq.heappush(h, s)
            speedSum += s
            if len(h) > k:
                speedSum -= h[0]
                heapq.heappop(h)
            res = max(res, speedSum*e)
        return res%(10**9 + 7)
