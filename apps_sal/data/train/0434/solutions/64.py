class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        i, r = 0, 1

        for j in range(len(nums)):
            if nums[j] == 0:
                r -= 1

            if r < 0:
                print('yes')
                if nums[i] == 0:
                    r += 1
                i += 1

        return j - i
