class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res=0
        sum1=1
        while sum1!=0:
            sum1 = 0
            for ii,i in enumerate(nums):
                if i%2!=0:
                    nums[ii]-=1
                    res+=1
                nums[ii] = nums[ii]//2
                sum1+=nums[ii]
            res+=1
        return res-1

