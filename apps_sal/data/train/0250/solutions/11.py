class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:

        # sorting workers based on the ration of wage and quality
        workers = sorted([float(w) / q, q] for w, q in zip(wage, quality))

        ans = float('inf')
        heap = []
        heapSum = 0

        for ratio, q in workers:
            heapq.heappush(heap, -q)  # max heap based off quality
            heapSum += q

            if len(heap) > K:  # if len of heap > K add largest heap elem
                heapSum += heapq.heappop(heap)

            if len(heap) == K:
                ans = min(ans, ratio * heapSum)

        return float(ans)
