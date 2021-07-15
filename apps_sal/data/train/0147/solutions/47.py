class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        heap = []
        total = 0
        pairs = list(zip(speed, efficiency))
        pairs.sort(key = lambda x: -x[1])
        res = 0
        MOD = 10 ** 9 + 7
        for i, (s, e) in enumerate(pairs):
            res = max(e * (total + s), res)
            if len(heap) < k - 1:
                heapq.heappush(heap, s)
                total += s
            elif heap and s > heap[0]:
                total -= heapq.heappop(heap)
                heapq.heappush(heap, s)
                total += s
        return res % MOD
