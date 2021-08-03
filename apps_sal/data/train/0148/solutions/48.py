class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(worker)
        jobs = sorted(zip(difficulty, profit))
        total = 0
        best = 0
        i = 0
        for ability in sorted(worker):
            while i < len(jobs) and ability >= jobs[i][0]:
                best = max(jobs[i][1], best)
                i += 1
            total += best
        return total
