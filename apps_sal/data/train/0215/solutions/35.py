class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True if nums[0] == 1 else False

        for i in range(1, len(nums)):
            nums[i] = gcd(nums[i], nums[i - 1])
            if nums[i] == 1:
                return True

        return False
