class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        '''
        Case 1. The first is that the subarray take only a middle part, and we know how to find the max subarray sum.
        Case2. The second is that the subarray take a part of head array and a part of tail array.
        
        in case two, you have two sub arrays, one at the front and one at the end. The middle segment actually now is the MIN
        subarray.
         The maximum result equals to the total sum minus the minimum subarray sum.
        '''
        total=0
        maxSum=A[0] #case1
        minSum=A[0] #case2
        curr_sum=0
        curr_sum_min=0
        for val in A:
            total+=val #calculate total sum\\
            #calculate max sum with kadanes normally for case1, assuming NO WRAP
            curr_sum=max(val,curr_sum+val)
            maxSum=max(maxSum,curr_sum)
            #now calculate the minsum
            curr_sum_min=min(val,curr_sum_min+val)
            minSum=min(minSum,curr_sum_min)
            print(maxSum)
        wrap_maxSum=total-minSum
  
        if maxSum>0:
            return max(wrap_maxSum,maxSum)
        else:
            return maxSum
