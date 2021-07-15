class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        nz = 0
        for num in nums:
            if num>0:
                nz+=1
       # print(nz)
        while nz>0:
           # print(nums, res)
            div2 = False
            for i in range(len(nums)):
                if nums[i]%2==1:
                    nums[i]-=1
                    res+=1
                    if nums[i]==0:
                        nz-=1
                if nums[i]>0:
                    div2 = True
                    nums[i]//=2
                    if nums[i]==0:
                        nz-=1
            #print('after', nums, nz)
            if div2:
                res+=1
        return res
