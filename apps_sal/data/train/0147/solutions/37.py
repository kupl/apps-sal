import heapq


class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        a = list(zip(efficiency, speed))
        a.sort(reverse=True)
        pq = []
        mp = s = 0
        for i in range(n):
            heapq.heappush(pq, a[i][1])
            s += a[i][1]
            if i >= k:
                s -= heapq.heappop(pq)
            mp = max(mp, s * a[i][0])
        return mp % (10 ** 9 + 7)
