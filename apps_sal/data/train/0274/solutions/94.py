class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i = 0
        j = 1
        n = len(nums)
        if n == 0:
            return 0
        mn = nums[0]
        mx = nums[0]
        l = 1
        while i <= j and j < n:
            if mn > nums[j]:
                mn = nums[j]
            if mx < nums[j]:
                mx = nums[j]
            if mx - mn <= limit:
                if j - i + 1 > l:
                    l = j - i + 1
            else:
                if mn == nums[i]:
                    mn = min(nums[i + 1:j + 1])
                if mx == nums[i]:
                    mx = max(nums[i + 1:j + 1])
                i += 1
            j += 1
        return l
