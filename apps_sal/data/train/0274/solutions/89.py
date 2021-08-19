class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums or len(nums) == 1:
            return len(nums)
        n = len(nums)
        i = 0
        j = 1
        res = 1
        min_in_window = nums[0]
        max_in_window = nums[0]
        while j < n:
            max_in_window = max(max_in_window, nums[j])
            min_in_window = min(min_in_window, nums[j])
            diff = abs(min_in_window - max_in_window)
            if diff <= limit:
                j += 1
                res = max(res, j - i)
            else:
                tmp = nums[i]
                while i <= j and i < n - 1 and (nums[i] == nums[i + 1]):
                    i += 1
                if nums[i] == min_in_window:
                    min_in_window = min(nums[i + 1:j + 1])
                if nums[i] == max_in_window:
                    max_in_window = max(nums[i + 1:j + 1])
                i += 1
                j += 1
        return res
