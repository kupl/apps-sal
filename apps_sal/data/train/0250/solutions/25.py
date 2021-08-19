import heapq as pq


class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        ratio = [[y / x, x] for (x, y) in zip(quality, wage)]
        ratio.sort(key=lambda x: x[0])
        i = 0
        l = []
        pq.heapify(l)
        r = 1
        s = 0
        while i < K:
            s += ratio[i][1]
            pq.heappush(l, -ratio[i][1])
            r = ratio[i][0]
            i += 1
        res = s * r
        n = len(quality)
        while i < n:
            r = ratio[i][0]
            num = ratio[i][1]
            pq.heappush(l, -num)
            val = -pq.heappop(l)
            s += num - val
            res = min(res, s * r)
            i += 1
        return res
