class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        pq = []
        engineers = list(zip(speed, efficiency))
        engineers.sort(key=lambda tup: -tup[1])
        performance = 0
        tot_speed = 0
        for engineer in engineers:
            min_efficiency = engineer[1]
            if len(pq) == k:
                if pq[0] < engineer[0]:
                    bad_speed = heapq.heappop(pq)
                    heapq.heappush(pq, engineer[0])
                    tot_speed = tot_speed - bad_speed + engineer[0]
            else:
                heapq.heappush(pq, engineer[0])
                tot_speed += engineer[0]
            performance = max(performance, tot_speed * min_efficiency)
        return performance % MOD
