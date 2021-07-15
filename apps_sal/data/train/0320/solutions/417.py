class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=0
        n=len(nums)
        while True:
            if len(set(nums))==1 and nums[0]==0:
                break
            for i in range(n):
                if nums[i]%2!=0 and nums[i]>0 and nums[i]!=0:
                    nums[i]=nums[i]-1
                    c+=1
            f=0
            for i in range(n):
                if nums[i]%2==0:
                    f+=1
            if len(set(nums))==1 and nums[0]==0:
                break
            if f==len(nums):
                for i in range(n):
                    if nums[i]%2==0 and nums[i]!=0:
                        nums[i]=nums[i]//2
                c+=1
        return c
