class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        jobs = len(jobDifficulty)
        if jobs < d:
            return -1
        
        opt = [[float('inf')] * jobs for _ in range(d)]
        opt[0][0] = jobDifficulty[0]
        for i in range(1, min(jobs, d)):
            opt[i][i] = opt[i-1][i-1] + jobDifficulty[i]
        for i in range(1, jobs):
            opt[0][i] = max(opt[0][i-1], jobDifficulty[i])
        print(opt)
        
        for k in range(1, jobs):
            for i in range(1, d):
                for x in range(1, k-i+2):  # k-x >= i-1
                    opt[i][k] = min(opt[i][k], 
                                   opt[i-1][k-x] + max(jobDifficulty[k-x+1: k+1]))
        print(opt)
        return opt[d-1][jobs-1]
