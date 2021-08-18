class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        profit = i = maxprofits = 0
        for ability in sorted(worker):
            while i < len(jobs) and ability >= jobs[i][0]:
                profit = max(jobs[i][1], profit)
                i += 1
            maxprofits += profit
        return maxprofits
