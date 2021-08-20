class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        a = [(s, e) for (s, e) in zip(speed, efficiency)]
        if k == 1:
            return max([s * e for (s, e) in a])
        a.sort(key=lambda x: -x[1])
        ret = 0
        q = []
        s_sum = 0
        for (s, e) in a:
            ret = max(ret, (s_sum + s) * e)
            if len(q) >= k - 1:
                if q[0] < s:
                    x = heapq.heappop(q)
                    s_sum = s_sum + s - x
                    heapq.heappush(q, s)
            else:
                heapq.heappush(q, s)
                s_sum += s
        return ret % (10 ** 9 + 7)
