from heapq import heappush, heappop


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        if len(wage) >= K:
            worker = []
            for i in range(0, len(quality)):
                rate = wage[i] / quality[i]
                worker.append((rate, quality[i]))
            worker.sort()
            base = 0
            i = 0
            q = []
            while i < K-1:
                base += worker[i][1]
                heappush(q, - worker[i][1])
                i += 1
            # print(worker)
            res = (base + worker[i][1]) * worker[i][0]
            while i < len(worker):
                # print((worker[i][0], base, res))
                rate = worker[i][0]
                res = min(res, (base + worker[i][1]) * rate)
                heappush(q, - worker[i][1])
                base += worker[i][1]
                val = heappop(q)
                base += val
                i += 1
            return res
        else:
            return -1.0

