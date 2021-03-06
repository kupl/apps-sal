class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        es = sorted(zip(efficiency, speed))
        result = 0
        heap = [0]
        s = 0
        for i in range(n - 1, -1, -1):
            if len(heap) < k:
                heapq.heappush(heap, es[i][1])
                s = s + es[i][1]
            elif es[i][1] > heap[0]:
                s = s + es[i][1] - heapq.heappushpop(heap, es[i][1])
            p = es[i][0] * s
            result = max(result, p)
        return result % MOD
