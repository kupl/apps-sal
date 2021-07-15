class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        N = len(A)
        if(N==0):
            return 0
        curr_max = A[0]
        global_max = A[0]
        curr_min = A[0]
        global_min = A[0]
        flag = 0 
        if(A[0]>=0):
            flag=1
    
        for i in range(1, N):
            if(A[i]>=0):
                flag=1
            if(curr_max >= 0):
                curr_max = curr_max + A[i]    
            else:
                curr_max = A[i]
            
            if(curr_min >= 0):
                curr_min = A[i]
            else:
                curr_min = curr_min + A[i] 
            
            if(curr_max > global_max):
                global_max = curr_max
            if(curr_min < global_min):
                global_min = curr_min
        if(flag==0):
            return max(A)
        return max(global_max, sum(A) - global_min)
