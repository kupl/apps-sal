class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # print(nums)

        ret = 0
        for i, x in enumerate(nums):
            if x % 2:
                ret += 1
                nums[i] -= 1

        if all(x == 0 for x in nums):
            return ret

        for i, x in enumerate(nums):
            nums[i] //= 2
        ret += 1
        #print(nums, ret)
        return ret + self.minOperations(nums)
