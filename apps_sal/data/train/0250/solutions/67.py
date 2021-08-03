class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:

        from fractions import Fraction

        wage_qual = sorted((Fraction(w, q), w, q) for w, q in zip(wage, quality))

        candidates = []
        psum = 0
        ans = float('inf')
        for ratio, w, q in wage_qual:
            heapq.heappush(candidates, -q)
            psum += q

            if len(candidates) > K:
                psum += heapq.heappop(candidates)

            if len(candidates) == K:
                ans = min(ans, psum * ratio)
        return ans
