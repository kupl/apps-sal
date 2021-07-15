'''
Time Complexity : O(n * d) where n = len(jobs)
'''
class Solution:
    def minDifficulty(self, jobs: List[int], d: int) -> int:
        if len(jobs) < d:
            return -1
        
        return self.topDown(jobs, d, 0, {})
    
    def topDown(self, jobs, d, index, memo):
        #This should never be the case as we schedule all
        #the rest of jobs on d = 1
        if d <= 0:
            return float('inf')
        # if len(jobs) - index + 1 < d:
        #     return float('inf')
        if d == 1:
            #if we still have some jobs on d = 1
            if index < len(jobs):
                return max(jobs[index: ])
            #If left with no job, we violate \"atleast a task every day\"
            return float('inf')
        
        if (d, index) in memo:
            return memo[(d, index)]
        
        mindiff = float('inf')
        
        #Each day allocate jobs from 0-th index to i-th index,so
        #difficulty for that day is max(jobs[index:i+1]), then
        #recurse for d-1 days and jobs[i+1:]
        #Finally, see which combination gives the minimum difficulty
        for i in range(index, len(jobs)):
            mindiff = min(mindiff, self.topDown(jobs, d - 1, i + 1, memo) + max(jobs[index : i + 1]))
        memo[(d, index)] = mindiff
        
        return mindiff
        

