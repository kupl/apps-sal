class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op=0
        sum1=sum(nums)
        while sum1!=0:
            for i in range(len(nums)):
                if nums[i]%2!=0:
                    nums[i]-=1
                    sum1-=1
                    op+=1
                    
            if sum1==0:
                return op
            
            for i in range(len(nums)):
                nums[i]//=2
            op+=1
            sum1/=2
            
        return op

