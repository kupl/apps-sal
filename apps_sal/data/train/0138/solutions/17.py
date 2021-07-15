class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pointer1=0
        pointer2=0
        res=0
        while(pointer1<len(nums)):
            if nums[pointer1]==0:
                pointer1+=1
                continue
            pointer2=pointer1
            count=0
            start=0
            end=0
            while(pointer2<len(nums) and nums[pointer2]!=0):
                if nums[pointer2]<0:
                    count+=1
                    if count==1:
                        start=pointer2
                    end=pointer2
                pointer2+=1
            if count%2==0:
                res=max(res,pointer2-pointer1)
            else:
                res=max(res,end-pointer1,pointer2-start-1)
            pointer1=pointer2
            
        return res
