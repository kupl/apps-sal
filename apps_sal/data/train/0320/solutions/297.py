class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        noz=0
        nosteps=0
        while(noz!=n):
            noz=0
            noe=0
            noo=0
            for i in range(len(nums)):
                if(nums[i] == 0):
                    noz+=1
                    noe+=1
                elif(nums[i]%2 == 0):
                    noe+=1
                    nums[i]=nums[i]//2
                else:
                    noo+=1
                    nums[i]-=1
                    nums[i]=nums[i]//2
            nosteps+=noo
            if(noz==n):
                break
            nosteps+=1
        return nosteps-1

