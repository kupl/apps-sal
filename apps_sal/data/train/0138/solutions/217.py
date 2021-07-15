class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # get the next zero or end
        # get the last idx of negative before zero and end
        # get how many negative numbers
        
        next_zero_or_end=[0]*(len(nums)+1)
        next_idx=len(nums)
        last_negative=[0]*(len(nums)+1)
        negative_idx=None
        state=0
        for i in range(len(nums)-1,-1,-1):
            num=nums[i]
            if num==0:
                next_idx=i
                state=0
            next_zero_or_end[i]=next_idx
            if state==0 and num<0:
                negative_idx=i
                state=1
            last_negative[i]=negative_idx
                
        ne_nums=[0] * (len(nums)+1)
        for i,num in enumerate(nums):
            ne_nums[i]=ne_nums[i-1]+(1 if num<0 else 0)
        res=0
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            j=next_zero_or_end[i]-1
            if (ne_nums[j]-ne_nums[i-1])%2==0:
                res=max(res,(j-i+1))
            else:
                j=last_negative[i]-1
                res=max(res,(j-i+1))
        return res
