class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        dp = [0] * len(nums)
        prev_sum = {0: -1}
        
        num_nonover = 0
        current_sum = 0
        
        for (index, num) in enumerate(nums):
            current_sum += num
            
            if current_sum - target in prev_sum:
                gain = dp[prev_sum[current_sum-target]] if prev_sum[current_sum-target] >= 0 else 0
                
                num_nonover = max(num_nonover, gain + 1)
                
                
            dp[index] = num_nonover
            prev_sum[current_sum] = index
            
        return num_nonover
            
        

