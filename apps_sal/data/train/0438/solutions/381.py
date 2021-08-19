import heapq


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        times = [0] * len(arr)
        for t, a in enumerate(arr):
            times[a - 1] = t
        # print(times)
        res = -1
        h = [(-a, i) for i, a in enumerate(times[:m])]
        heapq.heapify(h)
        maxtime = [-h[0][0]]
        for i in range(m, len(times)):
            heapq.heappush(h, (-times[i], i))
            while h[0][1] <= i - m:
                heapq.heappop(h)
            maxtime.append(-h[0][0])
        # print(maxtime)
        if maxtime[0] < times[m]:
            res = times[m]
        if maxtime[-1] < times[-m - 1]:
            res = max(res, times[-m - 1])
        for i in range(1, len(times) - m):
            if times[i - 1] > maxtime[i] and times[i + m] > maxtime[i]:
                res = max(res, min(times[i - 1], times[i + m]))
        return res
