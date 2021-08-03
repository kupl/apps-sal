class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        from fractions import Fraction

        # sorting workers based on the ration of wage and quality
        workers = sorted((Fraction(w, q), q, w) for q, w in zip(quality, wage))

        ans = float('inf')
        heap = []
        heapSum = 0

        for ration, q, w in workers:
            heapq.heappush(heap, -q)  # max heap based off quality
            heapSum += q

            if len(heap) > K:  # if len of heap > K add largest heap elem
                heapSum += heapq.heappop(heap)

            if len(heap) == K:
                ans = min(ans, ration * heapSum)

        return float(ans)
