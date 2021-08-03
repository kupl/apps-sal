class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        c = 0
        ind = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i + 1
                k = 0
                while j < len(nums) and nums[j] == 1:
                    k += 1
                    j += 1
                j = i - 1
                while j >= 0 and nums[j] == 1:
                    k += 1
                    j -= 1
                if k > c:
                    c = k
                    ind = i
        if ind == 0 and nums[ind] == 1:
            ind = len(nums) - 1
            c = len(nums) - 1
        return c
