class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        run_max = [float('-inf')]
        run_min = [float('inf')]
        # get run_max
        p = 1
        while p < len(A):
            run_max.append(max(run_max[-1], A[p-1]))
            p += 1
        # get run_min
        p = len(A) - 2
        while p > -1:
            run_min.append(min(run_min[-1], A[p+1]))
            p -= 1
        run_min = run_min[::-1]
        
        # find the pos that satisfies the condition.
        res = -1
        p = 0
        done = False
        while p < len(A) - 1 and not done:
            if A[p] <= run_min[p] and run_max[p] <= run_min[p]:
                res = p + 1
                done = True
                
            p += 1
        return  res
    
    

