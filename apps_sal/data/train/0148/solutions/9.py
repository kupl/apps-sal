class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        output = 0
        job = sorted(zip(difficulty, profit), reverse=True, key=lambda x: x[1])
        worker = sorted(worker, reverse=True)
        jobIndex = 0
        for workerCab in worker:
            while jobIndex < len(job):
                if job[jobIndex][0] <= workerCab:
                    break
                else:
                    jobIndex += 1
            if jobIndex < len(job):
                output = output + job[jobIndex][1]
        return output
