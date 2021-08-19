class Solution:

    def recursive(self, nums, left, right, target):
        print((left, right))
        if left > right:
            return False
        if left == right:
            return nums[left] == target
        if left + 1 == right:
            return nums[left] == target or nums[right] == target
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        if nums[mid] == nums[left] and nums[mid] == nums[right]:
            return self.recursive(nums, mid, right, target) or self.recursive(nums, left, mid, target)
        elif nums[mid] < target:
            if nums[right] >= target or (nums[left] <= nums[mid] and nums[mid] >= nums[right]):
                return self.recursive(nums, mid, right, target)
            else:
                return self.recursive(nums, left, mid, target)
        elif nums[left] <= target or (nums[right] >= nums[mid] and nums[mid] <= nums[left]):
            return self.recursive(nums, left, mid, target)
        else:
            return self.recursive(nums, mid, right, target)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        return self.recursive(nums, 0, len(nums) - 1, target)
