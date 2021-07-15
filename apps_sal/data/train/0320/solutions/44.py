class Solution:
    def minOperations(self, nums: List[int]) -> int:
        two,one = 0,0
        for n in nums:
            mul = 0
            while n :
                if  n%2 :
                    one += 1
                    n -= 1
                else:
                    mul += 1
                    n //= 2 
            two = max(two,mul)
        return one+two

    # @lru_cache(None)
    # def minOperations(self, nums: List[int]) -> int:
    #     return 0
    #     return self.helper(nums,-1,-1)
    # def helper(self, nums: List[int],op ,idx ) -> int:
    #     if op == 0:
    #         nums[idx] += 1
    #     elif op == 1:
    #         for i in range(len(nums)):
    #             nums[i] *= 2
    #     print(min([min(self.helper(nums,0,i),self.helper(nums,1,-1)) for i in range(len(nums))]))
    #     # return min([min(self.minOperations(nums,0,i),self.minOperations(nums,1,-1)) for i in range(len(nums))])
    #     return 0


