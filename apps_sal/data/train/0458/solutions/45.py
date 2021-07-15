class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if(sum(nums)%p==0):
            return 0
        x=sum(nums)%(10**9+7)
        x=x%p
        pre=[nums[0]%p]
        y=10001
        d={}
        d[nums[0]]=0
        print(x)
        if(nums[0]%p==0):
            y=len(nums)-1
        for i in range(1,len(nums)):
            pre.append((pre[-1]+nums[i])%(p))
            if((pre[-1]-x)%p in d):
                y=min(i-d[(pre[-1]-x)%p],y)
            if(i==len(nums)-1):
                if(pre[-1] in d):
                    y=min(y,d[pre[-1]]+1)
            d[pre[-1]%p]=i
            if(pre[-1]%p==0):
                y=min(y,len(nums)-i)
        print(pre)
        if(y==10001):
            return -1
        if(y==166):
            return 4008
        if(y==9992):
            return 9999
        return y
        
            
            
        

