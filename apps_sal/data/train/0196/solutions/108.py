class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        
        if n == 1:
            return A[0]
        
        pre_sum = 0
        pre_min_sum = 0
        pre_max_sum = 0
        
        
        pre_max_sum_i = -1
        min_sum_left = -1
        min_sum_right = -1
        max_sum = float('-inf')
        min_sum = float('inf')
        
        for i, a in enumerate(A):
            pre_sum += a
            
            max_sum = max(max_sum, pre_sum - pre_min_sum)
            min_sum_tmp = pre_sum - pre_max_sum
            if min_sum_tmp < min_sum:
                min_sum = min_sum_tmp
                min_sum_right = i
                min_sum_left = pre_max_sum_i + 1
            
            pre_min_sum = min(pre_min_sum, pre_sum)
            if pre_sum > pre_max_sum:
                pre_max_sum = pre_sum
                pre_max_sum_i = i
        
        total = sum(A)
        
        if total == min_sum and min_sum_left == 0 and min_sum_right == n - 1:
            return max_sum
        return max(max_sum, total - min_sum)
        
                
            
        
        
        

