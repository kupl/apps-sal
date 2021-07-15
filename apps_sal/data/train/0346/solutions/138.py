class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        d = {0:1}
        s = 0
        count = 0
        for i in range(len(nums)):
            
            nums[i]%=2
            s += nums[i]
            if not s in d:
                d[s]=0
            d[s]+=1
            if s-k in d:
                count += d[s-k]
                
        return count
                
            
        
            
        
        

