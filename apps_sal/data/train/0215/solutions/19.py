class Solution:

    def isGoodArray(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            nums[i] = gcd(nums[i], nums[i - 1]) if i > 0 else nums[0]
        return nums[-1] == 1
