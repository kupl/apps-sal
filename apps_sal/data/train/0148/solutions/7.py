class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        max_v = max(max(difficulty), max(worker))
        n = len(difficulty)
        best = [0] * (max_v + 1)
        for i in range(n):
            d = difficulty[i]
            p = profit[i]
            best[d] = max(best[d], p)
        for i in range(1, max_v + 1):
            best[i] = max(best[i - 1], best[i])
        s = 0
        for d in worker:
            s += best[d]
        return s
