class Solution:

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <= 3:
            return sum(nums)
        nums.sort()
        diff = float('inf')
        for (idx, num) in enumerate(nums[:-2]):
            if idx >= 1 and num == nums[idx - 1]:
                continue
            (start, end) = (idx + 1, len(nums) - 1)
            while start < end:
                temp_sum = nums[start] + nums[end]
                new_target = target - num
                if temp_sum == new_target:
                    return target
                elif temp_sum > new_target:
                    end -= 1
                else:
                    start += 1
                if abs(new_target - temp_sum) < diff:
                    if new_target - temp_sum < 0:
                        sign = -1
                    else:
                        sign = 1
                    diff = abs(new_target - temp_sum)
        return target - sign * diff
