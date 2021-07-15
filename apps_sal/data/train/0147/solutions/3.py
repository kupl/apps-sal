class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        teams = sorted(zip(efficiency, speed), reverse=True)
        pq = []
        max_perf = s = 0
        for i in range(n):
            heapq.heappush(pq, teams[i][1])
            s += teams[i][1]
            if i >= k:
                s -= heapq.heappop(pq)
            max_perf = max(max_perf, s * teams[i][0])
        return max_perf % (10 ** 9 + 7)
