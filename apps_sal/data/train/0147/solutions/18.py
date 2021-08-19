class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # Sort engineer by efficiency
        # for all engineer higher than efficiency x,
        # keep the ones with high speed
        if n == 0:
            return 0

        engineers = [[speed[i], efficiency[i]] for i in range(n)]
        engineers.sort(key=lambda x: x[1], reverse=True)

        mod = 1000000007
        pq = []
        sum_speed = 0
        min_efficiency = engineers[0][1]
        max_performance = 0
        for e in engineers:
            heapq.heappush(pq, e)
            sum_speed += e[0]
            if len(pq) > k:
                tmp = heapq.heappop(pq)
                sum_speed -= tmp[0]
                if tmp != e:  # The newly added engineer might be eliminated
                    min_efficiency = e[1]
            else:
                min_efficiency = e[1]

            max_performance = max(max_performance, sum_speed * min_efficiency)

        return max_performance % mod
