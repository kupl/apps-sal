class Solution:
    def minOperations(self, nums: List[int]) -> int:
#         The number of operation 0 equals to the total number of bits \"1\".
#         The number of operation 1 equals to maximum bit length - 1.
        
        return sum(bin(a).count('1') for a in nums) + len(bin(max(nums))) - 3
        
        # notfinish = True
        # count = 0
        # while notfinish:
        #     notfinish = False 
        #     for i,n in enumerate(nums):
        #         if n%2:
        #             nums[i] = (nums[i]-1)//2
        #             count += 1
        #             if nums[i]>0:
        #                 notfinish = True
        #         elif nums[i]>0:
        #             nums[i] = nums[i]//2
        #             notfinish = True
        #     if notfinish:
        #         count += 1
        #     print(nums,count)
        # return count

