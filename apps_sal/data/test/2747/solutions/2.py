class Solution:

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        (left, right) = (0, len(nums) - 1)
        while left <= right:
            mid = (left + right) // 2
            print(('mid:', mid))
            if nums[mid] == target:
                print('hello')
                if mid == 0 or nums[mid - 1] < target:
                    result.append(mid)
                    break
                else:
                    right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        (left, right) = (0, len(nums) - 1)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid + 1] > target:
                    result.append(mid)
                    break
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if len(result) == 0:
            return [-1, -1]
        return result
