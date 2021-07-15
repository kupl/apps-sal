class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # count = 0
        # l =[0]*len(nums)
        # while nums != l:
        #     flag = 0
        #     for i in range(len(nums)):
        #         if nums[i]%2 != 0:
        #             flag = 1
        #             nums[i] = nums[i]-1
        #             count+=1
        #             break
        #     if flag == 0:
        #         nums = [int(e/2) for e in nums]
        #         count+=1
        # return count
        ans = 0
        bns = 0
        for x in nums:
            b = bin(x)
            ans += b.count('1')
            if x:
                bns = max(bns, len(b) - 2)
        return ans + max(bns-1,0)

