class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = list(zip(difficulty, profit))
        jobs = sorted(jobs, key=lambda x: x[0])
        worker.sort()
        idx = 0
        ans = 0
        p = 0
        for skill in worker:
            while idx < len(jobs) and jobs[idx][0] <= skill:
                p = max(p, jobs[idx][1])
                idx += 1
            ans += p
        return ans
        
    
    

