class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker = sorted(worker)
        jobs = sorted([(-1,0)]+[(difficulty[i],profit[i])for i in range(len(difficulty))])
        job_nums = len(jobs)
        maxProfit = 0
        job_index = 0
        res = 0
        for ability in worker:
            while job_index < job_nums-1 and ability>= jobs[job_index+1][0]:
                job_index+=1
                maxProfit = max(maxProfit,jobs[job_index][1])
            res+=maxProfit
        return res
            
        
        

