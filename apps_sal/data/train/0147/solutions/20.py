import heapq


class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        comb = [(speed[i], efficiency[i]) for i in range(n)]
        comb.sort(key=lambda x: -x[1])
        total_speed = 0
        ans = 0
        pq = []
        for i in range(n):
            heapq.heappush(pq, comb[i][0])
            total_speed += comb[i][0]
            if len(pq) > k:
                total_speed -= heapq.heappop(pq)
            low_eff = comb[i][1]
            ans = max(ans, total_speed * low_eff)
        return ans % mod
