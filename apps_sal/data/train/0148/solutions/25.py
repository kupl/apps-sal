from bisect import bisect


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        maxp = 0
        maxpa = []
        for difficulty, profit in sorted(zip(difficulty, profit), key=lambda x: x[0]):
            maxp = max(maxp, profit)
            maxpa.append((difficulty, maxp))

        total = 0
        for w in worker:
            ind = bisect(maxpa, (w, float('inf')))
            if ind > 0:
                total += maxpa[ind - 1][1]

        return total
