import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        pairs = list(zip(efficiency, speed))
        pairs.sort(key = lambda x: (-x[0], -x[1]))
        arr = []
        res = 0
        sum_spd = 0
        for eff, spd in pairs:
            if len(arr) < k:
                sum_spd += spd
                heapq.heappush(arr, spd)
            else:
                if spd > arr[0]:
                    sum_spd += spd - heapq.heappushpop(arr, spd)
            res = max(res, sum_spd*eff)
        return res % (10**9 + 7)

