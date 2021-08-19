class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        ratios = [[wi / qi, qi] for (wi, qi) in zip(wage, quality)]
        ratios.sort(reverse=True)
        res = float('inf')
        quality.sort()
        for (ratio, q) in ratios:
            quality.remove(q)
            candidates = quality[:K - 1]
            if len(candidates) < K - 1:
                break
            ans = ratio * (q + sum(candidates))
            res = min(res, ans)
        return res
