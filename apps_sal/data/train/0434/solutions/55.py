class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        z = [0]
        a = 0
        c = 0
        if nums.count(1) == len(nums):
            return len(nums) - 1
        for i in range(len(nums)):
            if a == 1 and nums[i] == 0:
                z.append(c)
                c = (i) - (l + 1)
                a = 1
                l = i
            elif nums[i] == 0:
                a = a + 1
                l = i
            elif nums[i] == 1:
                c = c + 1
        z.append(c)
        return max(z)
