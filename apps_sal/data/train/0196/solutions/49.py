class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # max(the max subarray sum, the total sum - the min subarray sum)
        max_sum = -float('inf')
        cur_max = -float('inf')
        total_sum = 0
        cur_min = float('inf')
        min_sum = float('inf')
        for i in A:
            total_sum += i
            
            cur_max = max(cur_max + i, i)
            cur_min = min(cur_min + i, i)
            
            max_sum = max(max_sum, cur_max)
            min_sum = min(min_sum, cur_min)
            
        if total_sum - min_sum == 0:
            return max_sum
        return max(max_sum, total_sum - min_sum) 
