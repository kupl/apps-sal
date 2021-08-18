class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        if 0 in nums and 1 in nums:
            longest = 0
            i = nums.index(0)

            while True:

                if 0 in nums[:i][::-1]:
                    left_side = nums[:i][::-1].index(0)

                else:

                    left_side = len(nums[:i][::-1])

                if 0 in nums[i + 1:]:
                    right_side = nums[i + 1:].index(0)

                else:
                    right_side = len(nums[i + 1:])

                longest = max(left_side + right_side, longest)

                try:
                    i = nums[i + 1:].index(0) + i + 1
                except:
                    break

            return longest

        elif sum(nums) == 0:
            return 0

        elif sum(nums) == len(nums):
            return(len(nums) - 1)
