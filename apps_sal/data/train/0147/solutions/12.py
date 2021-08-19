class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        items = sorted(zip(speed, efficiency), key=lambda item: (-item[1], -item[0]))
        heap = []
        s = 0
        res = 0
        for item in items:
            if len(heap) < k or item[0] > heap[0][0]:
                if len(heap) == k:
                    popped = heapq.heappop(heap)
                    s -= popped[0]
                heapq.heappush(heap, item)
                s += item[0]
                res = max(res, s * item[1])
        return res % (10 ** 9 + 7)
