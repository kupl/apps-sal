class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        res = 0
        nums.sort()
        ln = len(nums)
        i = 0
        j = ln-1
        md = pow(10,9)+7
        
        while i <= j:
            if nums[i]+nums[j]<= target:
                res = (res + pow(2, j-i, md))%md
                i += 1
            else:
                j -= 1
        return res
    
            
                    
                    
            
            
        

