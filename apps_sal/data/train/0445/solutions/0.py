class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        else:
            nums.sort()
            threeZero = nums[-1] - nums[3]
            twoOne = nums[-2] - nums[2]
            oneTwo = nums[-3] - nums[1]
            zeroThree = nums[-4] - nums[0]
            return min(threeZero, twoOne, oneTwo, zeroThree)
