from heapq import heappush, heappop


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        M = 10**9 + 7
        eff_pq = []
        sp_pq = []
        speed_sum = 0
        for idx, eff in enumerate(efficiency):
            heappush(eff_pq, (-eff, idx))

        res = 0
        while len(eff_pq) > 0:
            neg_eff, idx = heappop(eff_pq)
            eff = -neg_eff
            heappush(sp_pq, speed[idx])
            speed_sum += speed[idx]

            if len(sp_pq) > k:
                sp_pop = heappop(sp_pq)
                speed_sum -= sp_pop

            res = max(res, eff * speed_sum)

        return res % M
