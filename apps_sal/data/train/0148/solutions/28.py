class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        mDifficulty = {}
        
        for i in range(len(difficulty)):
            d = difficulty[i]
            if difficulty[i] not in mDifficulty:
                mDifficulty[d] = 0
            mDifficulty[d] = max(mDifficulty[d], profit[i])
        
        jobs = []
        for key, value in mDifficulty.items():
            jobs.append([key, value]) 
            
        jobs.sort(key=lambda job:job[0])
        
        for i in range(1, len(jobs)):
            jobs[i][1] = max(jobs[i][1], jobs[i - 1][1])
            
        worker.sort()
        start = len(jobs) - 1
        count = 0
        
        for i in range(len(worker) - 1, - 1, -1):
            while worker[i] < jobs[start][0] and start >= 0:
                start -= 1
            if start < 0:
                break
            count += jobs[start][1]
            
        return count
