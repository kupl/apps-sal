class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_pos_len = 0
        max_neg_len = 0
        if nums[0] > 0: max_pos_len = 1
        if nums[0] < 0: max_neg_len = 1
        max_len = max(0, max_pos_len)
        
        for i in range(1, len(nums)):
            if nums[i] > 0: 
                max_pos_len += 1
                max_neg_len += (max_neg_len > 0)
            elif nums[i] < 0: 
                max_neg_len, max_pos_len = max_pos_len+1, max_neg_len+(max_neg_len > 0)
            elif nums[i] == 0: 
                max_pos_len = max_neg_len = 0
            
            max_len = max(max_len, max_pos_len)
        
        return max_len

