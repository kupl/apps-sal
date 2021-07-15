class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        
        noofones = 0
        m = 0
        lastoneslen = 0
        
        for i in nums:
            if i == 1:
                noofones += 1
            else:
                m = max(m, noofones+lastoneslen)
                lastoneslen = noofones
                noofones = 0
        
        m = max(m, noofones+lastoneslen)
        
        if m == len(nums):
            m -= 1
        
        return m
        
        
#         max_ones_len = 0
#         num_of_ones = 0
#         last_ones_len = 0
        
#         for num in nums:
#             if num == 1:
#                 num_of_ones +=1
#             else:
#                 max_ones_len = max(max_ones_len, last_ones_len + num_of_ones)
#                 last_ones_len = num_of_ones
#                 num_of_ones = 0
        
#         max_ones_len = max(max_ones_len, last_ones_len + num_of_ones)
        
#         if max_ones_len == len(nums):
#             max_ones_len -= 1
            
#         return max_ones_len

