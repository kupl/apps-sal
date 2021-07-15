class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        len1_prev=0
        len1=0
        i=0
        res=0
        zc=0#number of zeros in the middle
        while i<len(nums):
            if nums[i]==1:
                len1+=1
            else:
                res=max(res,len1+len1_prev)
                if zc==0:
                    len1_prev=len1
                    len1=0
                    zc=1
                elif zc==1:
                    if len1>0:
                        len1_prev=len1
                        len1=0
                        zc=1
                    else:
                        len1=0
                        len1_prev=0
                        zc=0
            i+=1
                    
                    
        res=max(res,len1+len1_prev)
        res=min(len(nums)-1,res)
        
        return res
                    
            

