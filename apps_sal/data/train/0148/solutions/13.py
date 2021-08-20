class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        best = 0
        tot = 0
        worker.sort()
        for (d, p) in sorted(zip(difficulty, profit)):
            while worker and d > worker[0]:
                tot += best
                worker.pop(0)
            best = max(best, p)
        tot += best * len(worker)
        return tot
