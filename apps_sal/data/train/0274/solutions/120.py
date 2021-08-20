class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        smallest = largest = nums[0]
        (start, end, window) = (0, 1, 1)
        while end < len(nums):
            (smallest, largest) = (min(smallest, nums[end]), max(largest, nums[end]))
            if largest - smallest <= limit:
                window = max(window, end - start + 1)
            else:
                if nums[start] == smallest:
                    smallest = min(nums[start + 1:end + 1])
                if nums[start] == largest:
                    largest = max(nums[start + 1:end + 1])
                start += 1
            end += 1
        return window
