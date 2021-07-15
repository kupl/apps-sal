class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        ss = sum(nums)
        ans=0
        while(ss>0):
            for i in range(n):
                if nums[i]%2!=0:
                    ans+=1
                    nums[i]-=1
                    ss-=1
            if ss>0:
                for i in range(n):
                    nums[i]//=2
                    ss-=nums[i]
                ans+=1
            
        return ans
