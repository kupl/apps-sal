class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        employees = sorted([[w / q, q] for (w, q) in zip(wage, quality)])
        print(employees)
        (res, totalOut) = (math.inf, 0)
        h = []
        for (rate, output) in employees:
            totalOut += output
            heapq.heappush(h, -output)
            if len(h) > K:
                totalOut += heapq.heappop(h)
            if len(h) == K:
                res = min(res, totalOut * rate)
        return res
