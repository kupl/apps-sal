class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        M = 10 ** 9 + 7
        
        heap = []
        ans = t = 0
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            t += s
            heapq.heappush(heap, s)
            if len(heap) == k+1:
                t -= heapq.heappop(heap)
            ans = max(ans, t * e)
        return ans % M
