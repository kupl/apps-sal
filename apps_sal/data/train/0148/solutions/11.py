class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = []
        total = 0

        for i in range(len(profit)):
            jobs.append([difficulty[i], profit[i]])
        print(jobs)

        worker.sort()
        jobs.sort()
        i = 0
        best = 0

        for work in worker:
            while i < len(jobs) and work >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            total += best

        return total
