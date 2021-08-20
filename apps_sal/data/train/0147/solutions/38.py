from heapq import heappush, heappop


class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        people = [[speed[i], efficiency[i]] for i in range(n)]
        people.sort(key=lambda x: -x[1])
        res = 0
        h = []
        total_speed = 0
        for (i, (s, e)) in enumerate(people):
            heappush(h, s)
            total_speed += s
            if len(h) > k:
                total_speed -= heappop(h)
            res = max(res, total_speed * e)
        return res % mod
