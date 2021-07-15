class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = [[difficulty[i],profit[i]] for i in range(len(difficulty))]
        jobs.sort()
        
        worker.sort()
        
        ans, best ,i = 0, 0,0
        
        
        for skill in worker:
            while i < (len(jobs)) and skill >= jobs[i][0]:
                best = max(best,jobs[i][1])
                i += 1
            ans += best
        return ans
