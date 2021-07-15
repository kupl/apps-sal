class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        return sum(abs(a-b) for a,b in zip(nums,nums[1:])) + max(max(abs(nums[0]-b)-abs(a-b) for a,b in zip(nums,nums[1:])),max(abs(nums[-1]-a)-abs(a-b) for a,b in zip(nums,nums[1:])),2*(max(min(a,b) for a,b in zip(nums,nums[1:]))-min(max(a,b) for a,b in zip(nums,nums[1:]))))
