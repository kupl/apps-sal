class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job = sorted(zip(difficulty, profit))
        best = 0
        i = 0
        profit = 0
        for work in sorted(worker):
            while i < len(difficulty) and job[i][0] <= work:
                best = max(best, job[i][1])
                i += 1
            profit += best
        return profit
