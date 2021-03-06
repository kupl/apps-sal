class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        eff_speed = sorted(zip(efficiency, speed), reverse=True)
        n = len(eff_speed)
        i = 0
        speed_h = []
        speed_sum = 0
        max_perf = 0
        start = 0
        while i < n:
            while i == start or (i < n and eff_speed[i][0] == eff_speed[i - 1][0]):
                heapq.heappush(speed_h, eff_speed[i][1])
                speed_sum += eff_speed[i][1]
                if len(speed_h) > k:
                    speed_sum -= heapq.heappop(speed_h)
                i += 1
            start = i
            cur_efficiency = eff_speed[i - 1][0]
            max_perf = max(max_perf, cur_efficiency * speed_sum)
        return max_perf % mod
