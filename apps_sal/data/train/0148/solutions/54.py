class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted([(difficulty[i], profit[i]) for i in range(len(difficulty))], key=lambda x: x[0])
        worker = sorted(worker)
        jobPointer = 0
        workerPointer = 0
        maxProfit = 0
        totalProfit = 0
        while True:
            if workerPointer >= len(worker):
                break
            talent = worker[workerPointer]
            if jobPointer >= len(jobs) or jobs[jobPointer][0] > talent:
                totalProfit += maxProfit
                workerPointer += 1
            else:
                if jobs[jobPointer][1] > maxProfit:
                    maxProfit = jobs[jobPointer][1]
                jobPointer += 1
        return totalProfit
