class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        left = []
        total = 0
        for n in nums:
            if n == 0:
                total = 0
            else:
                total += n
            left.append(total)
        right = []
        total = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                total = 0
            else:
                total += nums[i]
            right.append(total)
        right = right[::-1]
        curMax = 0
        for i in range(len(nums) - 2):
            curMax = max(left[i] + right[i + 2], curMax)
        return curMax
