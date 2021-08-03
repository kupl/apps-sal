class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) == 1 and limit >= 0:
            return 1

        longest_subarray = 0

        right = 0
        left = 0

        min_val = nums[left]
        max_val = nums[left]

        min_dq = []
        max_dq = []

        while right < len(nums):

            while len(min_dq) > 0 and min_dq[-1] > nums[right]:
                min_dq.pop()
            min_dq.append(nums[right])

            while len(max_dq) > 0 and max_dq[-1] < nums[right]:
                max_dq.pop()
            max_dq.append(nums[right])

            min_val = min_dq[0]
            max_val = max_dq[0]

            if abs(min_val - max_val) > limit:
                if min_dq[0] == nums[left]:
                    min_dq.pop(0)

                if max_dq[0] == nums[left]:
                    max_dq.pop(0)

                left += 1

            longest_subarray = max(longest_subarray, right - left + 1)
            right += 1

        return longest_subarray
